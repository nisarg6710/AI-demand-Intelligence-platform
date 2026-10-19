import json
import sqlite3
from pathlib import Path

import pytest

from deployment.demo_api import repository


SOURCE_COLUMNS = {
    "analytics_sales_summary": ("total_records", "total_sales", "average_sales", "minimum_sales", "maximum_sales"),
    "analytics_monthly_sales": ("year", "month", "total_sales"),
    "analytics_store_performance": ("store_id", "total_sales", "average_sales", "peak_sales"),
    "analytics_product_performance": ("item_id", "total_sales"),
    "analytics_category_performance": ("cat_id", "total_sales"),
    "analytics_department_performance": ("dept_id", "total_sales"),
    "analytics_weekday_sales": ("weekday", "total_sales"),
}
FIXTURE_GENERATION = "20261019T000000Z_" + "b" * 32


def _observed_schema():
    result = {}
    for table in repository.APPROVED_SOURCE_TABLES:
        result[table] = []
        for ordinal, name in enumerate(SOURCE_COLUMNS[table], 1):
            identifier = name.endswith("_id") or name == "weekday"
            is_average = name == "average_sales"
            result[table].append({
                "column_name": name,
                "ordinal_position": ordinal,
                "data_type": "varchar" if identifier else "decimal" if is_average or name == "total_sales" else "int",
                "column_type": "varchar(32)" if identifier else "decimal(18,6)" if is_average else "decimal(32,0)" if name == "total_sales" else "int",
                "is_nullable": "YES",
                "numeric_precision": 18 if is_average else 32 if name == "total_sales" else None,
                "numeric_scale": 6 if is_average else 0 if name == "total_sales" else None,
                "column_key": "",
            })
    return result


def _write_manifest(directory: Path, manifest: dict):
    manifest["outputs"]["manifest_pointer_size_bytes"] = 0
    for _ in range(10):
        encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
        size = len(encoded)
        if manifest["outputs"]["manifest_pointer_size_bytes"] == size:
            break
        manifest["outputs"]["manifest_pointer_size_bytes"] = size
    (directory / "aggregate_current.json").write_bytes(encoded)


@pytest.fixture
def snapshot_directory(tmp_path):
    directory = tmp_path / "snapshot"
    directory.mkdir()
    database_name = f"aggregate_snapshot_{FIXTURE_GENERATION}.sqlite"
    database = directory / database_name
    connection = sqlite3.connect(database)
    try:
        connection.executescript("""
            CREATE TABLE aggregate_sales_summary (record_count INTEGER NOT NULL, total_units INTEGER NOT NULL, average_units_per_fact_row REAL NOT NULL, minimum_units_per_fact_row INTEGER NOT NULL, maximum_units_per_fact_row INTEGER NOT NULL);
            CREATE TABLE aggregate_monthly_sales (year INTEGER NOT NULL, month INTEGER NOT NULL, total_units INTEGER NOT NULL, PRIMARY KEY (year, month)) WITHOUT ROWID;
            CREATE TABLE aggregate_store_performance (store_id TEXT PRIMARY KEY, total_units INTEGER NOT NULL, average_units_per_fact_row REAL NOT NULL, peak_fact_row_units INTEGER NOT NULL) WITHOUT ROWID;
            CREATE TABLE aggregate_product_performance (item_id TEXT PRIMARY KEY, total_units INTEGER NOT NULL) WITHOUT ROWID;
            CREATE TABLE aggregate_category_performance (cat_id TEXT PRIMARY KEY, total_units INTEGER NOT NULL) WITHOUT ROWID;
            CREATE TABLE aggregate_department_performance (dept_id TEXT PRIMARY KEY, total_units INTEGER NOT NULL) WITHOUT ROWID;
            CREATE TABLE aggregate_weekday_performance (weekday TEXT PRIMARY KEY, total_units INTEGER NOT NULL) WITHOUT ROWID;
            INSERT INTO aggregate_sales_summary VALUES (4, 10, 2.5, 0, 5);
            INSERT INTO aggregate_monthly_sales VALUES (2024, 1, 4), (2024, 2, 6);
            INSERT INTO aggregate_store_performance VALUES ('S1', 6, 3.0, 5), ('S2', 4, 2.0, 4);
            INSERT INTO aggregate_product_performance VALUES ('P1', 6), ('P2', 4);
            INSERT INTO aggregate_category_performance VALUES ('C1', 6), ('C2', 4);
            INSERT INTO aggregate_department_performance VALUES ('D1', 10);
            INSERT INTO aggregate_weekday_performance VALUES
                ('Monday', 4), ('Tuesday', 6), ('Wednesday', 0), ('Thursday', 0),
                ('Friday', 0), ('Saturday', 0), ('Sunday', 0);
        """)
        connection.commit()
    finally:
        connection.close()

    output_counts = {
        "aggregate_sales_summary": 1,
        "aggregate_monthly_sales": 2,
        "aggregate_store_performance": 2,
        "aggregate_product_performance": 2,
        "aggregate_category_performance": 2,
        "aggregate_department_performance": 1,
        "aggregate_weekday_performance": 7,
    }
    source_counts = {source: output_counts[output] for source, output in repository.SOURCE_TO_OUTPUT.items()}
    group_checks = {table: True for table in repository.GROUP_TABLES}
    manifest = {
        "format_version": repository.SUPPORTED_FORMAT_VERSION,
        "transformation_validation_contract_version": repository.SUPPORTED_CONTRACT_VERSION,
        "mode": "aggregate_only",
        "generation_id": FIXTURE_GENERATION,
        "generated_at_utc": "2026-10-19T00:00:00+00:00",
        "definition_fingerprint": "a" * 64,
        "source": {
            "database": "demand_intelligence",
            "tables": list(repository.APPROVED_SOURCE_TABLES),
            "live_schema_fingerprint": "",
            "scope": "Fixture of stored materialized aggregates",
            "freshness_verified": False,
            "freshness_note": "Fixture freshness is deliberately unverified",
            "units": "sales values represent units sold, not currency or revenue",
            "observed_columns": _observed_schema(),
        },
        "available_metrics": ["aggregate unit summaries"],
        "unavailable_metrics": ["daily sales", "transaction details"],
        "source_table_row_counts": source_counts,
        "validation": {
            "passed": True,
            "freshness_verified": False,
            "stored_summary_record_count": 4,
            "stored_summary_total_units": 10,
            "group_keys_unique": group_checks,
            "group_unit_totals_match_stored_summary": group_checks,
            "weekday_groups_complete": True,
            "source_table_row_counts": source_counts,
            "group_sums_units": {table: 10 for table in repository.GROUP_TABLES},
        },
        "optimizer_plan_fingerprint": {"collected": False, "value": None, "meaning": "No optimizer plan is used."},
        "outputs": {
            "database_file": database_name,
            "database_size_bytes": database.stat().st_size,
            "table_row_counts": output_counts,
            "schemas": {name: list(columns) for name, columns in repository.OUTPUT_SCHEMAS.items()},
            "manifest_pointer": "aggregate_current.json",
            "manifest_pointer_size_bytes": 0,
        },
        "elapsed_seconds": {"aggregate_table_read_and_validation": 0.01, "sqlite_build_and_validation": 0.01},
    }
    manifest["source"]["live_schema_fingerprint"] = repository._schema_fingerprint(manifest["source"]["observed_columns"])
    manifest["outputs"]["database_size_bytes"] = database.stat().st_size
    _write_manifest(directory, manifest)
    return directory
