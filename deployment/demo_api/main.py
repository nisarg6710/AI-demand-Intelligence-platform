
from pathlib import Path
import json
import math
from typing import Any
from datetime import date

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


# --------------------------------------------------
# Configuration
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

app = FastAPI(
    title="AI Demand Intelligence Platform — Demo API",
    description=(
        "A public portfolio demo serving precomputed analytics snapshots. "
        "It does not query the production database or call external AI APIs."
    ),
    version="1.0.0",
)

# Public demo API: no credentials are sent by the frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Load precomputed JSON snapshots
# --------------------------------------------------

DATA_FILES = {
    "monthly_sales": "monthly_sales.json",
    "sales_summary": "sales_summary.json",
    "top_stores": "top_stores.json",
    "category_performance": "category_performance.json",
    "department_performance": "department_performance.json",
    "top_products": "top_products.json",
    "weekday_sales": "weekday_sales.json",
    "model_comparison": "model_comparison.json",
    "historical_holdout": "historical_holdout_arima.json",
}

DATA: dict[str, Any] = {}


def load_snapshots() -> None:
    """Load and validate the demo snapshots at application startup."""
    for key, filename in DATA_FILES.items():
        path = DATA_DIR / filename

        if not path.is_file():
            raise RuntimeError(f"Required demo data file is missing: {path}")

        try:
            with path.open("r", encoding="utf-8-sig") as file:
                payload = json.load(file)
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeError(
                f"Could not load demo data file {filename}: {exc}"
            ) from exc

        if not isinstance(payload, dict) or payload.get("success") is not True:
            raise RuntimeError(f"Invalid API snapshot format: {filename}")

        if key == "model_comparison":
            rows = payload.get("data")
            required = {
                "model", "mae", "rmse", "mape", "train_time_s", "predict_time_s"
            }
            if not isinstance(payload.get("source"), str) or not isinstance(rows, list) or not rows:
                raise RuntimeError(f"Invalid model comparison format: {filename}")
            if any(not isinstance(row, dict) or not required.issubset(row) for row in rows):
                raise RuntimeError(f"Invalid model comparison rows: {filename}")
            for row in rows:
                if not isinstance(row["model"], str) or not row["model"]:
                    raise RuntimeError(f"Invalid model name in {filename}")
                try:
                    valid_metrics = all(
                        math.isfinite(float(row[field]))
                        for field in required - {"model"}
                    )
                except (TypeError, ValueError):
                    valid_metrics = False
                if not valid_metrics:
                    raise RuntimeError(f"Invalid model metrics in {filename}")

        if key == "historical_holdout":
            rows = payload.get("data")
            date_range = payload.get("date_range")
            required = {"forecast_date", "actual", "prediction"}
            if (
                payload.get("model_name") != "ARIMAModel"
                or payload.get("evaluation_type") != "historical_holdout_evaluation"
                or not isinstance(rows, list)
                or not rows
                or not isinstance(date_range, dict)
                or any(not isinstance(row, dict) or not required.issubset(row) for row in rows)
            ):
                raise RuntimeError(f"Invalid historical holdout format: {filename}")
            dates = [row["forecast_date"] for row in rows]
            if any(not isinstance(value, str) for value in dates):
                raise RuntimeError(f"Invalid historical holdout date values: {filename}")
            try:
                for value in dates:
                    date.fromisoformat(value)
                if any(
                    not math.isfinite(float(row[field]))
                    for row in rows
                    for field in ("actual", "prediction")
                ):
                    raise RuntimeError(f"Invalid historical holdout values: {filename}")
            except (TypeError, ValueError) as exc:
                raise RuntimeError(f"Invalid historical holdout values: {filename}") from exc
            if len(set(dates)) != len(dates) or dates != sorted(dates):
                raise RuntimeError(f"Historical holdout dates must be unique and sorted: {filename}")
            if date_range != {"start": dates[0], "end": dates[-1]}:
                raise RuntimeError(f"Invalid historical holdout date range: {filename}")

        DATA[key] = payload


@app.on_event("startup")
def startup_event() -> None:
    load_snapshots()


def snapshot(name: str) -> dict[str, Any]:
    """Return a defensive copy of a loaded snapshot."""
    return json.loads(json.dumps(DATA[name]))


# --------------------------------------------------
# Request models
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)


# --------------------------------------------------
# Health and information
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "success": True,
        "name": "AI Demand Intelligence Platform",
        "mode": "public_demo",
        "data_mode": "precomputed_snapshots",
        "database_connected": False,
        "external_ai_enabled": False,
        "available_pages": [
            "Dashboard",
            "Forecasting",
            "Analytics",
            "Chat",
            "Agents",
        ],
    }


@app.get("/health")
def health():
    return {
        "success": True,
        "status": "healthy",
        "mode": "public_demo",
        "data_mode": "precomputed_snapshots",
    }


# --------------------------------------------------
# Analytics endpoints
# --------------------------------------------------

@app.get("/analytics/monthly-sales")
def monthly_sales():
    return snapshot("monthly_sales")


@app.get("/analytics/summary")
def sales_summary():
    return snapshot("sales_summary")


@app.get("/analytics/top-stores")
def top_stores():
    return snapshot("top_stores")


@app.get("/analytics/category-performance")
def category_performance():
    return snapshot("category_performance")


@app.get("/analytics/department-performance")
def department_performance():
    return snapshot("department_performance")


@app.get("/analytics/top-products")
def top_products():
    return snapshot("top_products")


@app.get("/analytics/weekday-sales")
def weekday_sales():
    return snapshot("weekday_sales")


@app.post("/analytics")
def analytics(request: QuestionRequest):
    return {
        "success": True,
        "question": request.question,
        "response": (
            "This public demo uses precomputed sales analytics. "
            "Explore the Dashboard and Analytics pages for monthly sales, "
            "store performance, category performance, departments, products, "
            "and weekday trends. Arbitrary live database queries are not "
            "available in this demo."
        ),
    }


# --------------------------------------------------
# Forecasting demo endpoint
# --------------------------------------------------

@app.post("/forecast")
def forecast(request: QuestionRequest):
    return {
        "success": True,
        "question": request.question,
        "selected_action": "demo_forecast",
        "response": (
            "You are viewing the forecasting demonstration. The public demo "
            "does not run the production forecasting pipeline or train a model "
            "for each question. Use the available historical sales charts to "
            "explore the exported data. Live, question-specific forecasts are "
            "available only through the full local application."
        ),
    }


@app.get("/forecast/predictions")
def forecast_predictions():
    return {
        "success": True,
        "mode": "public_demo",
        "message": (
            "Question-specific model predictions are not generated by the "
            "public demo. Historical sales snapshots are available instead."
        ),
        "data": [],
    }


@app.get("/forecast/model-comparison")
def forecast_model_comparison():
    return snapshot("model_comparison")


@app.get("/forecast/historical-holdout")
def forecast_historical_holdout():
    return snapshot("historical_holdout")


# --------------------------------------------------
# Chat and report demo endpoints
# --------------------------------------------------

@app.post("/chat")
def chat(request: QuestionRequest):
    return {
        "success": True,
        "question": request.question,
        "selected_agents": ["Demo Assistant"],
        "response": (
            "This is the portfolio demo assistant. It can direct you to the "
            "available precomputed analytics, but it does not call Gemini, "
            "query MySQL, or execute the production agent workflow. "
            "Explore the Dashboard and Analytics pages for the exported "
            "sales results."
        ),
    }


@app.post("/report")
def report(request: QuestionRequest):
    return {
        "success": True,
        "question": request.question,
        "selected_agents": ["Demo Reporting"],
        "report": (
            "Public demo report: precomputed sales snapshots are available "
            "for monthly sales, store performance, category performance, "
            "department performance, products, and weekdays. This endpoint "
            "does not generate a live report from the production database."
        ),
    }
