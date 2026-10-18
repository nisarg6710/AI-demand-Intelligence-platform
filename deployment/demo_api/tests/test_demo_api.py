import csv
import json
import math
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from deployment.demo_api.main import app


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
ANALYTICS_FILES = {
    "monthly_sales": "monthly_sales.json",
    "sales_summary": "sales_summary.json",
    "top_stores": "top_stores.json",
    "category_performance": "category_performance.json",
    "department_performance": "department_performance.json",
    "top_products": "top_products.json",
    "weekday_sales": "weekday_sales.json",
}


@pytest.fixture()
def client():
    with TestClient(app) as test_client:
        yield test_client


def read_json(filename):
    return json.loads((DATA_DIR / filename).read_text(encoding="utf-8-sig"))


def test_all_demo_json_files_are_valid_and_have_success_flag():
    files = list(DATA_DIR.glob("*.json"))
    assert files
    for path in files:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        assert payload["success"] is True
        assert isinstance(payload.get("data"), list)


def test_analytics_snapshots_have_expected_fields_and_consistent_totals():
    expected_fields = {
        "monthly_sales": {"year", "month", "total_sales"},
        "top_stores": {"store_id", "total_sales"},
        "category_performance": {"cat_id", "total_sales"},
        "department_performance": {"dept_id", "total_sales"},
        "top_products": {"item_id", "total_sales"},
        "weekday_sales": {"weekday", "total_sales"},
    }
    payloads = {key: read_json(filename) for key, filename in ANALYTICS_FILES.items()}
    summary = payloads["sales_summary"]["data"]
    assert len(summary) == 1
    total_sales = summary[0]["total_sales"]
    for key, fields in expected_fields.items():
        rows = payloads[key]["data"]
        assert rows
        assert all(fields.issubset(row) for row in rows)
        if key != "top_products":
            assert sum(row["total_sales"] for row in rows) == pytest.approx(total_sales)
    assert len(payloads["monthly_sales"]["data"]) == 64
    assert len(payloads["top_stores"]["data"]) == 10
    assert len(payloads["category_performance"]["data"]) == 3
    assert len(payloads["department_performance"]["data"]) == 7
    assert len(payloads["top_products"]["data"]) == 10
    assert len(payloads["weekday_sales"]["data"]) == 7
    assert total_sales / summary[0]["total_records"] == pytest.approx(summary[0]["average_sales"], abs=1e-6)


def test_model_comparison_json_preserves_recorded_csv_results():
    payload = read_json("model_comparison.json")
    assert payload["source"] == "artifacts/classical_model_comparison.csv"
    fields = {"model", "mae", "rmse", "mape", "train_time_s", "predict_time_s"}
    assert len(payload["data"]) == 4
    assert all(fields.issubset(row) for row in payload["data"])
    with (DATA_DIR.parents[2] / "artifacts" / "classical_model_comparison.csv").open(encoding="utf-8-sig", newline="") as file:
        csv_rows = list(csv.DictReader(file))
    assert [row["model"] for row in payload["data"]] == [row["Model"] for row in csv_rows]
    for json_row, csv_row in zip(payload["data"], csv_rows):
        for json_key, csv_key in (("mae", "MAE"), ("rmse", "RMSE"), ("mape", "MAPE"), ("train_time_s", "Train Time"), ("predict_time_s", "Predict Time")):
            assert json_row[json_key] == pytest.approx(float(csv_row[csv_key]))


def test_historical_holdout_has_unique_finite_arima_rows_and_date_range():
    payload = read_json("historical_holdout_arima.json")
    assert payload["model_name"] == "ARIMAModel"
    assert payload["evaluation_type"] == "historical_holdout_evaluation"
    rows = payload["data"]
    dates = [row["forecast_date"] for row in rows]
    assert len(rows) == 383
    assert dates == sorted(set(dates))
    assert payload["date_range"] == {"start": dates[0], "end": dates[-1]}
    for row in rows:
        assert set(row) == {"forecast_date", "actual", "prediction"}
        assert math.isfinite(row["actual"])
        assert math.isfinite(row["prediction"])


def test_health_and_all_snapshot_endpoints(client):
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["mode"] == "public_demo"
    for filename in ANALYTICS_FILES.values():
        endpoint = {
            "monthly_sales.json": "/analytics/monthly-sales",
            "sales_summary.json": "/analytics/summary",
            "top_stores.json": "/analytics/top-stores",
            "category_performance.json": "/analytics/category-performance",
            "department_performance.json": "/analytics/department-performance",
            "top_products.json": "/analytics/top-products",
            "weekday_sales.json": "/analytics/weekday-sales",
        }[filename]
        response = client.get(endpoint)
        assert response.status_code == 200
        assert response.json() == read_json(filename)


def test_model_comparison_and_holdout_endpoints(client):
    comparison = client.get("/forecast/model-comparison")
    assert comparison.status_code == 200
    assert comparison.json() == read_json("model_comparison.json")
    holdout = client.get("/forecast/historical-holdout")
    assert holdout.status_code == 200
    assert holdout.json() == read_json("historical_holdout_arima.json")


def test_demo_post_endpoints_have_expected_schema_and_honest_labels(client):
    question = {"question": "Compare the available results."}
    analytics = client.post("/analytics", json=question).json()
    assert {"success", "question", "response"}.issubset(analytics)
    assert "precomputed" in analytics["response"].lower()

    forecast = client.post("/forecast", json=question).json()
    assert {"success", "question", "selected_action", "response"}.issubset(forecast)
    assert "does not run" in forecast["response"].lower()

    chat = client.post("/chat", json=question).json()
    assert {"success", "question", "selected_agents", "response"}.issubset(chat)
    assert "does not call gemini" in chat["response"].lower()

    report = client.post("/report", json=question).json()
    assert {"success", "question", "selected_agents", "report"}.issubset(report)
    assert "does not generate a live report" in report["report"].lower()


def test_cors_preflight_allows_public_frontend_origin(client):
    response = client.options(
        "/analytics/summary",
        headers={
            "Origin": "https://portfolio.example",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "*"
    assert "GET" in response.headers["access-control-allow-methods"]
