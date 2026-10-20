import json
import shutil
import sqlite3

import pytest

from deployment.demo_api.repository import (
    AggregateSnapshotRepository,
    APPROVED_SOURCE_TABLES,
    OUTPUT_SCHEMAS,
    SnapshotUnavailable,
)


def _rewrite_manifest(snapshot_dir, manifest):
    pointer = snapshot_dir / "aggregate_current.json"
    manifest["outputs"]["manifest_pointer_size_bytes"] = 0
    for _ in range(10):
        encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")
        size = len(encoded)
        if manifest["outputs"]["manifest_pointer_size_bytes"] == size:
            break
        manifest["outputs"]["manifest_pointer_size_bytes"] = size
    pointer.write_bytes(encoded)


def _read_manifest(snapshot_dir):
    return json.loads((snapshot_dir / "aggregate_current.json").read_text(encoding="utf-8"))


def test_repository_serves_all_approved_aggregates_and_metadata(snapshot_directory):
    repository = AggregateSnapshotRepository(snapshot_directory)
    assert repository.summary()["data"] == [{
        "total_records": 4,
        "total_sales": 10,
        "average_sales": 2.5,
        "minimum_sales": 0,
        "maximum_sales": 5,
    }]
    assert repository.monthly_sales()["data"] == [
        {"year": 2024, "month": 1, "total_sales": 4},
        {"year": 2024, "month": 2, "total_sales": 6},
    ]
    stores = repository.store_performance(limit=1)["data"]
    assert stores == [{"store_id": "S1", "total_sales": 6, "average_sales": 3.0, "peak_sales": 5}]
    assert repository.top_products(limit=1)["data"] == [{"item_id": "P1", "total_sales": 6}]
    assert repository.category_performance()["data"] == [
        {"cat_id": "C1", "total_sales": 6}, {"cat_id": "C2", "total_sales": 4}
    ]
    assert repository.department_performance()["data"] == [{"dept_id": "D1", "total_sales": 10}]
    assert [row["weekday"] for row in repository.weekday_performance()["data"]] == [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    metadata = repository.summary()
    assert metadata["data_source"] == "sqlite_aggregate_snapshot"
    assert metadata["freshness_verified"] is False
    assert metadata["snapshot_generation"] == "20261019T000000Z_" + "b" * 32
    assert metadata["units"] == "units sold; not currency or revenue"


@pytest.mark.parametrize("limit", [0, 101, True, "1; DROP TABLE aggregate_product_performance"])
def test_rank_limits_reject_invalid_or_injection_values(snapshot_directory, limit):
    repository = AggregateSnapshotRepository(snapshot_directory)
    with pytest.raises(ValueError, match="between 1 and 100"):
        repository.top_products(limit=limit)


def test_database_connections_are_read_only(snapshot_directory):
    repository = AggregateSnapshotRepository(snapshot_directory)
    connection = repository._connect()
    try:
        with pytest.raises(sqlite3.OperationalError):
            connection.execute("DELETE FROM aggregate_product_performance")
    finally:
        connection.close()
    assert repository.top_products()["data"]


def test_missing_and_malformed_pointer_fail_safely(tmp_path):
    with pytest.raises(SnapshotUnavailable, match="pointer"):
        AggregateSnapshotRepository(tmp_path)
    (tmp_path / "aggregate_current.json").write_text("{not json", encoding="utf-8")
    with pytest.raises(SnapshotUnavailable, match="malformed"):
        AggregateSnapshotRepository(tmp_path)


def test_missing_database_fails_safely(snapshot_directory):
    manifest = _read_manifest(snapshot_directory)
    (snapshot_directory / manifest["outputs"]["database_file"]).unlink()
    with pytest.raises(SnapshotUnavailable, match="database is missing"):
        AggregateSnapshotRepository(snapshot_directory)


def test_pointer_symlink_is_rejected(snapshot_directory, tmp_path):
    pointer = snapshot_directory / "aggregate_current.json"
    target = tmp_path / "pointer-target.json"
    target.write_bytes(pointer.read_bytes())
    pointer.unlink()
    try:
        pointer.symlink_to(target)
    except (OSError, NotImplementedError) as exc:
        pytest.skip(f"File symlinks are unavailable: {exc}")
    with pytest.raises(SnapshotUnavailable, match="pointer.*unsafe"):
        AggregateSnapshotRepository(snapshot_directory)


def test_database_symlink_is_rejected(snapshot_directory, tmp_path):
    manifest = _read_manifest(snapshot_directory)
    database = snapshot_directory / manifest["outputs"]["database_file"]
    target = tmp_path / "database-target.sqlite"
    shutil.copyfile(database, target)
    database.unlink()
    try:
        database.symlink_to(target)
    except (OSError, NotImplementedError) as exc:
        pytest.skip(f"File symlinks are unavailable: {exc}")
    with pytest.raises(SnapshotUnavailable, match="database is missing or unsafe"):
        AggregateSnapshotRepository(snapshot_directory)


@pytest.mark.parametrize("mutation", [
    "missing_generation", "missing_source", "missing_outputs", "missing_validation",
    "invalid_fingerprint",
])
def test_missing_or_malformed_required_manifest_fields_fail(snapshot_directory, mutation):
    manifest = _read_manifest(snapshot_directory)
    if mutation == "missing_generation":
        del manifest["generation_id"]
    elif mutation == "missing_source":
        del manifest["source"]
    elif mutation == "missing_outputs":
        del manifest["outputs"]
    elif mutation == "missing_validation":
        del manifest["validation"]
    else:
        manifest["definition_fingerprint"] = "not-a-sha256"
    if mutation == "missing_outputs":
        (snapshot_directory / "aggregate_current.json").write_text(
            json.dumps(manifest), encoding="utf-8"
        )
    else:
        _rewrite_manifest(snapshot_directory, manifest)
    with pytest.raises(SnapshotUnavailable):
        AggregateSnapshotRepository(snapshot_directory)


def test_unsupported_contract_and_wrong_source_table_list_fail(snapshot_directory):
    manifest = _read_manifest(snapshot_directory)
    manifest["transformation_validation_contract_version"] = "unsupported"
    _rewrite_manifest(snapshot_directory, manifest)
    with pytest.raises(SnapshotUnavailable, match="contract is unsupported"):
        AggregateSnapshotRepository(snapshot_directory)

    manifest = _read_manifest(snapshot_directory)
    manifest["transformation_validation_contract_version"] = "1.1.0"
    manifest["source"]["tables"] = ["sales_fact"]
    _rewrite_manifest(snapshot_directory, manifest)
    with pytest.raises(SnapshotUnavailable, match="table allowlist"):
        AggregateSnapshotRepository(snapshot_directory)


@pytest.mark.parametrize("mutation,expected_error", [
    ("extra_table", "table set"),
    ("wrong_schema", "schema is incompatible"),
    ("unexpected_view", "unexpected schema objects"),
    ("unexpected_trigger", "unexpected schema objects"),
    ("unexpected_index", "unexpected schema objects"),
])
def test_unexpected_tables_and_schema_mismatches_fail(snapshot_directory, mutation, expected_error):
    manifest = _read_manifest(snapshot_directory)
    database = snapshot_directory / manifest["outputs"]["database_file"]
    connection = sqlite3.connect(database)
    try:
        if mutation == "extra_table":
            connection.execute("CREATE TABLE unexpected (id INTEGER)")
        elif mutation == "wrong_schema":
            connection.execute("DROP TABLE aggregate_category_performance")
            connection.execute("CREATE TABLE aggregate_category_performance (wrong_column TEXT)")
        elif mutation == "unexpected_view":
            connection.execute("CREATE VIEW unexpected_view AS SELECT cat_id FROM aggregate_category_performance")
        elif mutation == "unexpected_trigger":
            connection.execute(
                "CREATE TRIGGER unexpected_trigger AFTER INSERT ON aggregate_category_performance "
                "BEGIN SELECT 1; END"
            )
        else:
            connection.execute("CREATE INDEX unexpected_index ON aggregate_category_performance(total_units)")
        connection.commit()
    finally:
        connection.close()
    manifest["outputs"]["database_size_bytes"] = database.stat().st_size
    _rewrite_manifest(snapshot_directory, manifest)
    with pytest.raises(SnapshotUnavailable, match=expected_error):
        AggregateSnapshotRepository(snapshot_directory)


def test_database_path_cannot_escape_snapshot_directory(snapshot_directory):
    manifest = _read_manifest(snapshot_directory)
    manifest["outputs"]["database_file"] = "..\\outside.sqlite"
    _rewrite_manifest(snapshot_directory, manifest)
    with pytest.raises(SnapshotUnavailable, match="filename"):
        AggregateSnapshotRepository(snapshot_directory)


def test_manifest_declares_exact_schema_and_sources(snapshot_directory):
    manifest = _read_manifest(snapshot_directory)
    assert manifest["source"]["tables"] == list(APPROVED_SOURCE_TABLES)
    assert manifest["outputs"]["schemas"] == {table: list(columns) for table, columns in OUTPUT_SCHEMAS.items()}


def test_new_repository_reads_pointer_generation_changed_between_requests(snapshot_directory):
    first = AggregateSnapshotRepository(snapshot_directory)
    original_generation = first.metadata["snapshot_generation"]
    manifest = _read_manifest(snapshot_directory)
    old_database = snapshot_directory / manifest["outputs"]["database_file"]
    generation = "20261019T000001Z_" + "c" * 32
    new_database_name = f"aggregate_snapshot_{generation}.sqlite"
    shutil.copyfile(old_database, snapshot_directory / new_database_name)
    manifest["generation_id"] = generation
    manifest["generated_at_utc"] = "2026-10-19T00:00:01+00:00"
    manifest["outputs"]["database_file"] = new_database_name
    manifest["outputs"]["database_size_bytes"] = (snapshot_directory / new_database_name).stat().st_size
    _rewrite_manifest(snapshot_directory, manifest)

    subsequent_request = AggregateSnapshotRepository(snapshot_directory)
    assert first.metadata["snapshot_generation"] == original_generation
    assert subsequent_request.metadata["snapshot_generation"] == generation
    assert subsequent_request.summary()["data"][0]["total_sales"] == 10


def test_relative_environment_path_is_resolved_from_service_root(snapshot_directory, tmp_path, monkeypatch):
    service_root = tmp_path / "service"
    service_root.mkdir()
    shutil.copytree(snapshot_directory, service_root / "snapshot")
    monkeypatch.setattr("deployment.demo_api.repository.SERVICE_ROOT", service_root)
    monkeypatch.setenv("PUBLIC_DEMO_SNAPSHOT_DIR", "snapshot")
    monkeypatch.chdir(tmp_path)

    repository = AggregateSnapshotRepository.from_environment()

    assert repository.snapshot_dir == (service_root / "snapshot").resolve()
    assert repository.summary()["data"][0]["total_sales"] == 10


@pytest.mark.parametrize("configured_value", ["", "   ", "\t\n"])
def test_empty_or_whitespace_environment_path_fails_without_fallback(
    snapshot_directory, monkeypatch, configured_value
):
    monkeypatch.setattr("deployment.demo_api.repository.DEFAULT_SNAPSHOT_DIR", snapshot_directory)
    monkeypatch.setattr("deployment.demo_api.repository.PACKAGED_SNAPSHOT_DIR", snapshot_directory)
    monkeypatch.setenv("PUBLIC_DEMO_SNAPSHOT_DIR", configured_value)

    with pytest.raises(SnapshotUnavailable, match="must not be empty or whitespace-only") as error:
        AggregateSnapshotRepository.from_environment()

    assert error.value.stage == "configuration"


def test_unset_environment_prefers_local_exports_when_both_sources_exist(
    snapshot_directory, tmp_path, monkeypatch
):
    local_exports = tmp_path / "exports" / "public_demo"
    packaged_snapshot = tmp_path / "service" / "snapshot"
    local_exports.parent.mkdir(parents=True)
    packaged_snapshot.parent.mkdir(parents=True)
    shutil.copytree(snapshot_directory, local_exports)
    shutil.copytree(snapshot_directory, packaged_snapshot)
    monkeypatch.setattr("deployment.demo_api.repository.DEFAULT_SNAPSHOT_DIR", local_exports)
    monkeypatch.setattr("deployment.demo_api.repository.PACKAGED_SNAPSHOT_DIR", packaged_snapshot)
    monkeypatch.delenv("PUBLIC_DEMO_SNAPSHOT_DIR", raising=False)

    repository = AggregateSnapshotRepository.from_environment()

    assert repository.snapshot_dir == local_exports.resolve()


def test_packaged_snapshot_is_fallback_when_local_exports_are_absent(snapshot_directory, tmp_path, monkeypatch):
    service_root = tmp_path / "service"
    service_root.mkdir()
    shutil.copytree(snapshot_directory, service_root / "snapshot")
    monkeypatch.setattr("deployment.demo_api.repository.SERVICE_ROOT", service_root)
    monkeypatch.setattr("deployment.demo_api.repository.PACKAGED_SNAPSHOT_DIR", service_root / "snapshot")
    monkeypatch.setattr("deployment.demo_api.repository.DEFAULT_SNAPSHOT_DIR", tmp_path / "missing-exports")
    monkeypatch.delenv("PUBLIC_DEMO_SNAPSHOT_DIR", raising=False)

    repository = AggregateSnapshotRepository.from_environment()

    assert repository.snapshot_dir == (service_root / "snapshot").resolve()
    assert repository.metadata["freshness_verified"] is False
