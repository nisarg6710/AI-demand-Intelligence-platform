"""Read-only access to the published public-demo SQLite aggregate snapshot.

Set ``PUBLIC_DEMO_SNAPSHOT_DIR`` to the directory containing
``aggregate_current.json`` and its generation database. Locally, the default is
the repository's ``exports/public_demo`` directory. This module never repairs,
regenerates, or writes to a snapshot.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
import re
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from typing import Any


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SERVICE_ROOT = Path(__file__).resolve().parent
DEFAULT_SNAPSHOT_DIR = REPOSITORY_ROOT / "exports" / "public_demo"
PACKAGED_SNAPSHOT_DIR = SERVICE_ROOT / "snapshot"
SNAPSHOT_DIR_ENV = "PUBLIC_DEMO_SNAPSHOT_DIR"
SUPPORTED_FORMAT_VERSION = 1
SUPPORTED_CONTRACT_VERSION = "1.1.0"
APPROVED_SOURCE_TABLES = (
    "analytics_sales_summary",
    "analytics_monthly_sales",
    "analytics_store_performance",
    "analytics_product_performance",
    "analytics_category_performance",
    "analytics_department_performance",
    "analytics_weekday_sales",
)
REQUIRED_SOURCE_COLUMNS = {
    "analytics_sales_summary": ("total_records", "total_sales", "average_sales", "minimum_sales", "maximum_sales"),
    "analytics_monthly_sales": ("year", "month", "total_sales"),
    "analytics_store_performance": ("store_id", "total_sales", "average_sales", "peak_sales"),
    "analytics_product_performance": ("item_id", "total_sales"),
    "analytics_category_performance": ("cat_id", "total_sales"),
    "analytics_department_performance": ("dept_id", "total_sales"),
    "analytics_weekday_sales": ("weekday", "total_sales"),
}
OUTPUT_SCHEMAS = {
    "aggregate_sales_summary": (
        "record_count", "total_units", "average_units_per_fact_row",
        "minimum_units_per_fact_row", "maximum_units_per_fact_row",
    ),
    "aggregate_monthly_sales": ("year", "month", "total_units"),
    "aggregate_store_performance": (
        "store_id", "total_units", "average_units_per_fact_row", "peak_fact_row_units",
    ),
    "aggregate_product_performance": ("item_id", "total_units"),
    "aggregate_category_performance": ("cat_id", "total_units"),
    "aggregate_department_performance": ("dept_id", "total_units"),
    "aggregate_weekday_performance": ("weekday", "total_units"),
}
OUTPUT_COLUMN_DEFS = {
    "aggregate_sales_summary": (
        ("record_count", "INTEGER", 1, 0), ("total_units", "INTEGER", 1, 0),
        ("average_units_per_fact_row", "REAL", 1, 0),
        ("minimum_units_per_fact_row", "INTEGER", 1, 0), ("maximum_units_per_fact_row", "INTEGER", 1, 0),
    ),
    "aggregate_monthly_sales": (
        ("year", "INTEGER", 1, 1), ("month", "INTEGER", 1, 2), ("total_units", "INTEGER", 1, 0),
    ),
    "aggregate_store_performance": (
        ("store_id", "TEXT", 1, 1), ("total_units", "INTEGER", 1, 0),
        ("average_units_per_fact_row", "REAL", 1, 0), ("peak_fact_row_units", "INTEGER", 1, 0),
    ),
    "aggregate_product_performance": (("item_id", "TEXT", 1, 1), ("total_units", "INTEGER", 1, 0)),
    "aggregate_category_performance": (("cat_id", "TEXT", 1, 1), ("total_units", "INTEGER", 1, 0)),
    "aggregate_department_performance": (("dept_id", "TEXT", 1, 1), ("total_units", "INTEGER", 1, 0)),
    "aggregate_weekday_performance": (("weekday", "TEXT", 1, 1), ("total_units", "INTEGER", 1, 0)),
}
SOURCE_TO_OUTPUT = {
    "analytics_sales_summary": "aggregate_sales_summary",
    "analytics_monthly_sales": "aggregate_monthly_sales",
    "analytics_store_performance": "aggregate_store_performance",
    "analytics_product_performance": "aggregate_product_performance",
    "analytics_category_performance": "aggregate_category_performance",
    "analytics_department_performance": "aggregate_department_performance",
    "analytics_weekday_sales": "aggregate_weekday_performance",
}
GROUP_TABLES = tuple(table for table in APPROVED_SOURCE_TABLES if table != "analytics_sales_summary")
WEEKDAY_ORDER = "CASE weekday WHEN 'Monday' THEN 1 WHEN 'Tuesday' THEN 2 WHEN 'Wednesday' THEN 3 WHEN 'Thursday' THEN 4 WHEN 'Friday' THEN 5 WHEN 'Saturday' THEN 6 WHEN 'Sunday' THEN 7 ELSE 8 END"


class SnapshotUnavailable(RuntimeError):
    """The active snapshot is missing, invalid, or incompatible."""

    def __init__(self, message: str, *, stage: str = "snapshot_validation"):
        super().__init__(message)
        self.stage = stage


def _schema_fingerprint(observed_schema: dict[str, Any]) -> str:
    canonical = []
    for table in APPROVED_SOURCE_TABLES:
        columns = observed_schema.get(table)
        if not isinstance(columns, list):
            raise SnapshotUnavailable("Snapshot source schema metadata is incomplete")
        normalized = []
        for column in columns:
            if not isinstance(column, dict):
                raise SnapshotUnavailable("Snapshot source schema metadata is malformed")
            normalized.append({
                key: column.get(key)
                for key in (
                    "column_name", "ordinal_position", "data_type", "column_type",
                    "is_nullable", "numeric_precision", "numeric_scale", "column_key",
                )
            })
        normalized.sort(key=lambda item: (
            item["ordinal_position"] is None,
            item["ordinal_position"] or 0,
            str(item["column_name"]),
        ))
        canonical.append({"table_name": table, "columns": normalized})
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


class AggregateSnapshotRepository:
    """Validate one active generation and serve allowlisted read operations."""

    def __init__(self, snapshot_dir: str | Path | None = None):
        self._diagnostic_stage = "configuration"
        try:
            self._initialize(snapshot_dir)
        except SnapshotUnavailable as exc:
            if exc.stage != "snapshot_validation":
                raise
            raise SnapshotUnavailable(str(exc), stage=self._diagnostic_stage) from exc

    def _initialize(self, snapshot_dir: str | Path | None) -> None:
        configured = snapshot_dir
        if configured is None:
            configured = os.environ.get(SNAPSHOT_DIR_ENV)
            if configured is None:
                # Prefer the normal local export when it exists. In a clean Render
                # checkout only the packaged snapshot is available beneath rootDir.
                configured = DEFAULT_SNAPSHOT_DIR if DEFAULT_SNAPSHOT_DIR.is_dir() else PACKAGED_SNAPSHOT_DIR
        if isinstance(configured, str) and not configured.strip():
            raise SnapshotUnavailable(
                f"{SNAPSHOT_DIR_ENV} must not be empty or whitespace-only"
            )
        try:
            configured_path = Path(configured).expanduser()
            if not configured_path.is_absolute():
                configured_path = SERVICE_ROOT / configured_path
            self.snapshot_dir = configured_path.resolve(strict=False)
        except (OSError, RuntimeError) as exc:
            raise SnapshotUnavailable("Configured snapshot directory is invalid") from exc
        if not self.snapshot_dir.is_dir():
            raise SnapshotUnavailable("Configured snapshot directory is unavailable")

        self._diagnostic_stage = "pointer_read"
        self.pointer_path = self.snapshot_dir / "aggregate_current.json"
        if self.pointer_path.is_symlink() or not self.pointer_path.is_file():
            raise SnapshotUnavailable("Active snapshot pointer is missing or unsafe")
        try:
            self.manifest = json.loads(self.pointer_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise SnapshotUnavailable("Active snapshot pointer is malformed or unreadable") from exc
        self._diagnostic_stage = "manifest_validation"
        self._validate_manifest()

        self._diagnostic_stage = "database_resolution"
        database_name = self.manifest["outputs"]["database_file"]
        if (
            not isinstance(database_name, str)
            or not database_name
            or Path(database_name).name != database_name
            or "/" in database_name
            or "\\" in database_name
        ):
            raise SnapshotUnavailable("Snapshot database filename is invalid")
        self.database_path = self.snapshot_dir / database_name
        if self.database_path.is_symlink() or not self.database_path.is_file():
            raise SnapshotUnavailable("Manifest-referenced snapshot database is missing or unsafe")
        try:
            resolved_database = self.database_path.resolve(strict=True)
            resolved_database.relative_to(self.snapshot_dir.resolve(strict=True))
        except (OSError, ValueError) as exc:
            raise SnapshotUnavailable("Snapshot database resolves outside the configured directory") from exc
        self.database_path = resolved_database
        try:
            if self.database_path.stat().st_size != self.manifest["outputs"]["database_size_bytes"]:
                raise SnapshotUnavailable("Snapshot database size does not match its manifest")
            if self.pointer_path.stat().st_size != self.manifest["outputs"]["manifest_pointer_size_bytes"]:
                raise SnapshotUnavailable("Snapshot pointer size does not match its manifest")
        except OSError as exc:
            raise SnapshotUnavailable("Snapshot files could not be inspected") from exc
        self._diagnostic_stage = "sqlite_validation"
        self._validate_database()

    @classmethod
    def from_environment(cls) -> "AggregateSnapshotRepository":
        return cls()

    def _validate_manifest(self) -> None:
        manifest = self.manifest
        if not isinstance(manifest, dict):
            raise SnapshotUnavailable("Snapshot manifest must be a JSON object")
        if manifest.get("format_version") != SUPPORTED_FORMAT_VERSION:
            raise SnapshotUnavailable("Snapshot format version is unsupported")
        if manifest.get("mode") != "aggregate_only":
            raise SnapshotUnavailable("Snapshot generation is not an aggregate-only generation")
        if manifest.get("transformation_validation_contract_version") != SUPPORTED_CONTRACT_VERSION:
            raise SnapshotUnavailable("Snapshot transformation/validation contract is unsupported")
        generation = manifest.get("generation_id")
        if not isinstance(generation, str) or not re.fullmatch(r"\d{8}T\d{6}Z_[0-9a-f]{32}", generation):
            raise SnapshotUnavailable("Snapshot generation identifier is invalid")
        fingerprint = manifest.get("definition_fingerprint")
        if not isinstance(fingerprint, str) or not re.fullmatch(r"[0-9a-f]{64}", fingerprint):
            raise SnapshotUnavailable("Snapshot export-definition fingerprint is invalid")
        generated_at = manifest.get("generated_at_utc")
        try:
            timestamp = datetime.fromisoformat(generated_at) if isinstance(generated_at, str) else None
        except ValueError as exc:
            raise SnapshotUnavailable("Snapshot generation timestamp is invalid") from exc
        if timestamp is None or timestamp.tzinfo is None or timestamp.utcoffset() != timezone.utc.utcoffset(timestamp):
            raise SnapshotUnavailable("Snapshot generation timestamp must be UTC")

        source = manifest.get("source")
        if not isinstance(source, dict) or source.get("database") != "demand_intelligence":
            raise SnapshotUnavailable("Snapshot source provenance is invalid")
        if source.get("tables") != list(APPROVED_SOURCE_TABLES):
            raise SnapshotUnavailable("Snapshot source table allowlist does not match")
        if source.get("freshness_verified") is not False:
            raise SnapshotUnavailable("Snapshot must retain freshness_verified=false")
        if not isinstance(source.get("scope"), str) or not source["scope"].strip():
            raise SnapshotUnavailable("Snapshot scope metadata is missing")
        if not isinstance(source.get("freshness_note"), str) or not source["freshness_note"].strip():
            raise SnapshotUnavailable("Snapshot freshness limitation is missing")
        if source.get("units") != "sales values represent units sold, not currency or revenue":
            raise SnapshotUnavailable("Snapshot units metadata is invalid")
        observed = source.get("observed_columns")
        if not isinstance(observed, dict) or set(observed) != set(APPROVED_SOURCE_TABLES):
            raise SnapshotUnavailable("Snapshot observed schema is incomplete")
        for table, columns in observed.items():
            if not isinstance(columns, list) or any(not isinstance(column, dict) for column in columns):
                raise SnapshotUnavailable(f"Snapshot observed schema is malformed: {table}")
            required_metadata = {
                "column_name", "ordinal_position", "data_type", "column_type",
                "is_nullable", "numeric_precision", "numeric_scale", "column_key",
            }
            if any(
                not required_metadata.issubset(column)
                or not isinstance(column["column_name"], str)
                or not isinstance(column["ordinal_position"], int)
                or isinstance(column["ordinal_position"], bool)
                or not isinstance(column["data_type"], str)
                or not isinstance(column["column_type"], str)
                or not isinstance(column["is_nullable"], str)
                or (column["numeric_precision"] is not None and not isinstance(column["numeric_precision"], int))
                or (column["numeric_scale"] is not None and not isinstance(column["numeric_scale"], int))
                or (column["column_key"] is not None and not isinstance(column["column_key"], str))
                for column in columns
            ):
                raise SnapshotUnavailable(f"Snapshot observed schema metadata has invalid types: {table}")
            column_names = {column.get("column_name") for column in columns}
            if not set(REQUIRED_SOURCE_COLUMNS[table]).issubset(column_names):
                raise SnapshotUnavailable(f"Snapshot observed schema is missing required columns: {table}")
        if source.get("live_schema_fingerprint") != _schema_fingerprint(observed):
            raise SnapshotUnavailable("Snapshot live-schema fingerprint does not match its metadata")
        for field in ("available_metrics", "unavailable_metrics"):
            values = manifest.get(field)
            if not isinstance(values, list) or not values or any(not isinstance(value, str) or not value.strip() for value in values):
                raise SnapshotUnavailable(f"Snapshot {field} metadata is missing or invalid")

        outputs = manifest.get("outputs")
        if not isinstance(outputs, dict):
            raise SnapshotUnavailable("Snapshot output metadata is missing")
        expected_filename = f"aggregate_snapshot_{generation}.sqlite"
        if outputs.get("database_file") != expected_filename:
            raise SnapshotUnavailable("Snapshot database filename does not match its generation")
        if outputs.get("manifest_pointer") != "aggregate_current.json":
            raise SnapshotUnavailable("Snapshot pointer metadata is invalid")
        for field in ("database_size_bytes", "manifest_pointer_size_bytes"):
            if not isinstance(outputs.get(field), int) or isinstance(outputs[field], bool) or outputs[field] < 0:
                raise SnapshotUnavailable(f"Snapshot {field} is invalid")
        if outputs.get("schemas") != {name: list(columns) for name, columns in OUTPUT_SCHEMAS.items()}:
            raise SnapshotUnavailable("Snapshot output schema manifest is incompatible")

        output_counts = outputs.get("table_row_counts")
        source_counts = manifest.get("source_table_row_counts")
        if not isinstance(output_counts, dict) or set(output_counts) != set(OUTPUT_SCHEMAS):
            raise SnapshotUnavailable("Snapshot output row counts are incomplete")
        if not isinstance(source_counts, dict) or set(source_counts) != set(APPROVED_SOURCE_TABLES):
            raise SnapshotUnavailable("Snapshot source row counts are incomplete")
        if any(not isinstance(value, int) or isinstance(value, bool) or value < 0 for value in (*output_counts.values(), *source_counts.values())):
            raise SnapshotUnavailable("Snapshot row counts contain invalid values")
        if any(output_counts[output] != source_counts[source_name] for source_name, output in SOURCE_TO_OUTPUT.items()):
            raise SnapshotUnavailable("Snapshot source and output row counts disagree")

        validation = manifest.get("validation")
        if not isinstance(validation, dict) or validation.get("passed") is not True:
            raise SnapshotUnavailable("Snapshot manifest does not record successful validation")
        if validation.get("freshness_verified") is not False:
            raise SnapshotUnavailable("Snapshot validation must retain freshness_verified=false")
        if validation.get("weekday_groups_complete") is not True:
            raise SnapshotUnavailable("Snapshot weekday validation is incomplete")
        for field in ("group_keys_unique", "group_unit_totals_match_stored_summary"):
            checks = validation.get(field)
            if not isinstance(checks, dict) or set(checks) != set(GROUP_TABLES) or any(value is not True for value in checks.values()):
                raise SnapshotUnavailable(f"Snapshot validation results are incomplete: {field}")
        if validation.get("source_table_row_counts") != source_counts:
            raise SnapshotUnavailable("Snapshot validation row counts disagree with manifest")
        summary_count = validation.get("stored_summary_record_count")
        summary_units = validation.get("stored_summary_total_units")
        if (
            not isinstance(summary_count, int) or isinstance(summary_count, bool) or summary_count <= 0
            or not isinstance(summary_units, int) or isinstance(summary_units, bool)
        ):
            raise SnapshotUnavailable("Snapshot validated summary metadata is invalid")
        group_sums = validation.get("group_sums_units")
        if not isinstance(group_sums, dict) or set(group_sums) != set(GROUP_TABLES):
            raise SnapshotUnavailable("Snapshot group total validation metadata is incomplete")
        if any(not isinstance(value, int) or isinstance(value, bool) or value != summary_units for value in group_sums.values()):
            raise SnapshotUnavailable("Snapshot group totals do not match the stored summary")
        if output_counts["aggregate_sales_summary"] != 1:
            raise SnapshotUnavailable("Snapshot summary row count must be one")

    def _connect(self) -> sqlite3.Connection:
        try:
            connection = sqlite3.connect(self.database_path.as_uri() + "?mode=ro", uri=True, timeout=5)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA query_only = ON")
            return connection
        except sqlite3.Error as exc:
            raise SnapshotUnavailable("Snapshot database could not be opened read-only") from exc

    def _validate_database(self) -> None:
        try:
            with closing(self._connect()) as connection:
                integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
                if integrity != "ok":
                    raise SnapshotUnavailable("Snapshot SQLite integrity check failed")
                rows = connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
                ).fetchall()
                tables = {row["name"] for row in rows}
                if tables != set(OUTPUT_SCHEMAS):
                    raise SnapshotUnavailable("Snapshot SQLite table set is incompatible")
                unexpected_objects = connection.execute(
                    "SELECT type, name FROM sqlite_master "
                    "WHERE type IN ('view', 'trigger', 'index') AND name NOT LIKE 'sqlite_%'"
                ).fetchall()
                if unexpected_objects:
                    raise SnapshotUnavailable("Snapshot SQLite contains unexpected schema objects")
                for table, expected_columns in OUTPUT_SCHEMAS.items():
                    actual_definition = tuple(
                        (row["name"], row["type"].upper(), row["notnull"], row["pk"])
                        for row in connection.execute(f"PRAGMA table_info({table})")
                    )
                    if tuple(item[0] for item in actual_definition) != expected_columns or actual_definition != OUTPUT_COLUMN_DEFS[table]:
                        raise SnapshotUnavailable(f"Snapshot SQLite schema is incompatible: {table}")
                    actual_count = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                    expected_count = self.manifest["outputs"]["table_row_counts"][table]
                    if actual_count != expected_count:
                        raise SnapshotUnavailable(f"Snapshot SQLite row count disagrees with manifest: {table}")

                summary_rows = connection.execute(
                    "SELECT record_count, total_units, average_units_per_fact_row, "
                    "minimum_units_per_fact_row, maximum_units_per_fact_row "
                    "FROM aggregate_sales_summary"
                ).fetchall()
                if len(summary_rows) != 1:
                    raise SnapshotUnavailable("Snapshot summary must contain exactly one row")
                summary = summary_rows[0]
                count, units, average, minimum, maximum = tuple(summary)
                if (
                    not isinstance(count, int) or count <= 0
                    or not isinstance(units, int)
                    or not isinstance(average, (int, float)) or not math.isfinite(average)
                    or not isinstance(minimum, int) or not isinstance(maximum, int)
                    or minimum > average or average > maximum
                    or not math.isclose(average, units / count, rel_tol=1e-12, abs_tol=self._average_tolerance())
                ):
                    raise SnapshotUnavailable("Snapshot summary values are malformed or inconsistent")
                if count != self.manifest["validation"]["stored_summary_record_count"] or units != self.manifest["validation"]["stored_summary_total_units"]:
                    raise SnapshotUnavailable("Snapshot summary values disagree with validated manifest values")
                for table in OUTPUT_SCHEMAS:
                    if table == "aggregate_sales_summary":
                        continue
                    if table == "aggregate_monthly_sales":
                        invalid_rows = connection.execute(
                            "SELECT COUNT(*) FROM aggregate_monthly_sales "
                            "WHERE year IS NULL OR month IS NULL OR month < 1 OR month > 12 "
                            "OR typeof(year) != 'integer' OR typeof(month) != 'integer' "
                            "OR total_units IS NULL OR typeof(total_units) != 'integer'"
                        ).fetchone()[0]
                    else:
                        key_column = {
                            "aggregate_store_performance": "store_id",
                            "aggregate_product_performance": "item_id",
                            "aggregate_category_performance": "cat_id",
                            "aggregate_department_performance": "dept_id",
                            "aggregate_weekday_performance": "weekday",
                        }[table]
                        invalid_rows = connection.execute(
                            f"SELECT COUNT(*) FROM {table} WHERE {key_column} IS NULL "
                            f"OR typeof({key_column}) != 'text' OR total_units IS NULL "
                            "OR typeof(total_units) != 'integer'"
                        ).fetchone()[0]
                    if invalid_rows:
                        raise SnapshotUnavailable(f"Snapshot contains malformed rows: {table}")
                    total = connection.execute(f"SELECT COALESCE(SUM(total_units), 0) FROM {table}").fetchone()[0]
                    if total != units:
                        raise SnapshotUnavailable(f"Snapshot group totals disagree with summary: {table}")
                weekdays = {
                    row[0] for row in connection.execute("SELECT weekday FROM aggregate_weekday_performance")
                }
                if weekdays != {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}:
                    raise SnapshotUnavailable("Snapshot weekday groups are incomplete")
                store_metrics = connection.execute(
                    "SELECT average_units_per_fact_row, peak_fact_row_units FROM aggregate_store_performance"
                ).fetchall()
                if any(
                    not isinstance(row[0], (int, float)) or not math.isfinite(row[0])
                    or not isinstance(row[1], int) or row[1] < 0
                    for row in store_metrics
                ):
                    raise SnapshotUnavailable("Snapshot store metrics are malformed")
        except sqlite3.Error as exc:
            raise SnapshotUnavailable("Snapshot database validation failed") from exc

    def _metadata(self) -> dict[str, Any]:
        return {
            "data_source": "sqlite_aggregate_snapshot",
            "freshness_verified": False,
            "snapshot_generation": self.manifest["generation_id"],
            "units": "units sold; not currency or revenue",
        }

    @property
    def metadata(self) -> dict[str, Any]:
        return self._metadata()

    def _average_tolerance(self) -> float:
        columns = self.manifest["source"]["observed_columns"]["analytics_sales_summary"]
        average_column = next((column for column in columns if column.get("column_name") == "average_sales"), None)
        if average_column is None:
            raise SnapshotUnavailable("Snapshot summary average precision metadata is missing")
        scale = average_column.get("numeric_scale")
        if scale is None:
            return 1e-9
        if not isinstance(scale, int) or isinstance(scale, bool) or scale < 0:
            raise SnapshotUnavailable("Snapshot summary average precision metadata is invalid")
        return 0.5 * (10 ** -scale) + 1e-12

    def _rows(self, sql: str, parameters: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
        try:
            with closing(self._connect()) as connection:
                return [dict(row) for row in connection.execute(sql, parameters).fetchall()]
        except sqlite3.Error as exc:
            raise SnapshotUnavailable("Snapshot query failed") from exc

    @staticmethod
    def _validate_limit(limit: int) -> int:
        if type(limit) is not int or not 1 <= limit <= 100:
            raise ValueError("limit must be an integer between 1 and 100")
        return limit

    def _response(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        return {"success": True, "data": rows, **self._metadata()}

    def summary(self) -> dict[str, Any]:
        rows = self._rows(
            "SELECT record_count AS total_records, total_units AS total_sales, "
            "average_units_per_fact_row AS average_sales, "
            "minimum_units_per_fact_row AS minimum_sales, "
            "maximum_units_per_fact_row AS maximum_sales FROM aggregate_sales_summary"
        )
        return self._response(rows)

    def monthly_sales(self) -> dict[str, Any]:
        return self._response(self._rows(
            "SELECT year, month, total_units AS total_sales FROM aggregate_monthly_sales ORDER BY year, month"
        ))

    def store_performance(self, limit: int = 10) -> dict[str, Any]:
        limit = self._validate_limit(limit)
        return self._response(self._rows(
            "SELECT store_id, total_units AS total_sales, "
            "average_units_per_fact_row AS average_sales, peak_fact_row_units AS peak_sales "
            "FROM aggregate_store_performance ORDER BY total_units DESC, store_id LIMIT ?",
            (limit,),
        ))

    def top_products(self, limit: int = 10) -> dict[str, Any]:
        limit = self._validate_limit(limit)
        return self._response(self._rows(
            "SELECT item_id, total_units AS total_sales FROM aggregate_product_performance "
            "ORDER BY total_units DESC, item_id LIMIT ?",
            (limit,),
        ))

    def category_performance(self) -> dict[str, Any]:
        return self._response(self._rows(
            "SELECT cat_id, total_units AS total_sales FROM aggregate_category_performance "
            "ORDER BY total_units DESC, cat_id"
        ))

    def department_performance(self) -> dict[str, Any]:
        return self._response(self._rows(
            "SELECT dept_id, total_units AS total_sales FROM aggregate_department_performance "
            "ORDER BY total_units DESC, dept_id"
        ))

    def weekday_performance(self) -> dict[str, Any]:
        return self._response(self._rows(
            f"SELECT weekday, total_units AS total_sales FROM aggregate_weekday_performance ORDER BY {WEEKDAY_ORDER}"
        ))
