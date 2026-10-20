
from pathlib import Path
import json
import logging
import math
from typing import Any
from datetime import date

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

try:  # Works both as ``uvicorn main:app`` and as a repository package import.
    from .repository import AggregateSnapshotRepository, SnapshotUnavailable
    from .chat_router import ChatRoute, route_question
    from .forecasting import (
        DEFAULT_FORECAST_HORIZON,
        MAX_FORECAST_HORIZON,
        ForecastUnavailable,
        seasonal_naive_forecast,
    )
except ImportError:  # pragma: no cover - exercised by Render's service root.
    from repository import AggregateSnapshotRepository, SnapshotUnavailable
    from chat_router import ChatRoute, route_question
    from forecasting import (
        DEFAULT_FORECAST_HORIZON,
        MAX_FORECAST_HORIZON,
        ForecastUnavailable,
        seasonal_naive_forecast,
    )


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
    "model_comparison": "model_comparison.json",
    "historical_holdout": "historical_holdout_arima.json",
}

DATA: dict[str, Any] = {}
logger = logging.getLogger(__name__)


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


def analytics_repository() -> AggregateSnapshotRepository:
    try:
        return AggregateSnapshotRepository.from_environment()
    except SnapshotUnavailable as exc:
        cause = exc.__cause__
        while isinstance(cause, SnapshotUnavailable):
            cause = cause.__cause__
        cause_type = type(cause).__name__ if cause is not None else "none"
        # The detail is generated by repository validation code (never user input).
        # Keep paths, tracebacks, and exception internals out of the HTTP response.
        logger.error(
            "Public analytics snapshot validation failed: stage=%s error_type=%s cause_type=%s detail=%s",
            exc.stage,
            type(exc).__name__,
            cause_type,
            str(exc),
        )
        raise HTTPException(
            status_code=503,
            detail="The public analytics snapshot is unavailable or invalid.",
        ) from exc


# --------------------------------------------------
# Request models
# --------------------------------------------------

class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)


class ForecastRequest(QuestionRequest):
    horizon: int = Field(
        default=DEFAULT_FORECAST_HORIZON,
        strict=True,
        ge=1,
        le=MAX_FORECAST_HORIZON,
        description="Number of future months to compute, from 1 to 12.",
    )


# --------------------------------------------------
# Health and information
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "success": True,
        "name": "AI Demand Intelligence Platform",
        "mode": "public_demo",
        "data_mode": "sqlite_aggregate_snapshot_and_recorded_forecast_artifacts",
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


@app.get("/live")
def liveness():
    """Lightweight process liveness; does not assert analytics readiness."""
    return {"success": True, "status": "alive", "mode": "public_demo"}


@app.get("/health")
def health():
    """Readiness check used by Render; fail if the required snapshot is unusable."""
    try:
        repository = analytics_repository()
    except HTTPException as exc:
        raise HTTPException(
            status_code=503,
            detail={
                "success": False,
                "status": "not_ready",
                "mode": "public_demo",
                "data_mode": "sqlite_aggregate_snapshot",
            },
        ) from exc
    return {
        "success": True,
        "status": "healthy",
        "mode": "public_demo",
        "data_mode": "sqlite_aggregate_snapshot",
        **repository.metadata,
    }


# --------------------------------------------------
# Analytics endpoints
# --------------------------------------------------

@app.get("/analytics/monthly-sales")
def monthly_sales():
    return analytics_repository().monthly_sales()


@app.get("/analytics/summary")
def sales_summary():
    return analytics_repository().summary()


@app.get("/analytics/top-stores")
def top_stores(limit: int = Query(default=10, ge=1, le=100)):
    return analytics_repository().store_performance(limit)


@app.get("/analytics/category-performance")
def category_performance():
    return analytics_repository().category_performance()


@app.get("/analytics/department-performance")
def department_performance():
    return analytics_repository().department_performance()


@app.get("/analytics/top-products")
def top_products(limit: int = Query(default=10, ge=1, le=100)):
    return analytics_repository().top_products(limit)


@app.get("/analytics/weekday-sales")
def weekday_sales():
    return analytics_repository().weekday_performance()


def _execute_routed_question(
    route: ChatRoute,
    question: str,
    repository: AggregateSnapshotRepository,
) -> dict[str, Any]:
    if route.intent == "forecast_baseline":
        forecast_result = _compute_forecast(question, route.horizon, repository)
        return {**forecast_result, "data": forecast_result["forecast_periods"]}

    operations = {
        "summary": repository.summary,
        "monthly_sales": repository.monthly_sales,
        "top_stores": lambda: repository.store_performance(route.limit),
        "top_products": lambda: repository.top_products(route.limit),
        "category_performance": repository.category_performance,
        "department_performance": repository.department_performance,
        "weekday_performance": repository.weekday_performance,
    }
    return operations[route.intent]()


@app.post("/analytics")
def analytics(request: QuestionRequest):
    repository = analytics_repository()
    route = route_question(request.question)
    if route.intent is None:
        return {
            "success": True,
            "question": request.question,
            "response": f"{route.reason} Snapshot freshness against MySQL is unverified.",
            "supported": False,
            "intent_status": route.status,
            **repository.metadata,
        }

    try:
        result = _execute_routed_question(route, request.question, repository)
    except SnapshotUnavailable as exc:
        raise HTTPException(
            status_code=503,
            detail="The public analytics snapshot is unavailable or invalid.",
        ) from exc

    payload = {
        "success": True,
        "question": request.question,
        "response": _format_chat_answer(route, result["data"]),
        "supported": True,
        "intent_status": "supported",
        "intent": route.intent,
        "data": result["data"],
        **{key: result[key] for key in (
            "data_source", "freshness_verified", "snapshot_generation", "units"
        )},
    }
    if route.intent == "forecast_baseline":
        payload.update({
            "method": result["method"],
            "horizon": result["horizon"],
            "forecast_periods": result["forecast_periods"],
            "observed_period": result["observed_period"],
        })
    return payload


# --------------------------------------------------
# Forecasting demo endpoint
# --------------------------------------------------

@app.post("/forecast")
def forecast(request: ForecastRequest):
    repository = analytics_repository()
    return _compute_forecast(request.question, request.horizon, repository)


def _compute_forecast(question: str, horizon: int, repository: AggregateSnapshotRepository) -> dict[str, Any]:
    try:
        monthly_result = repository.monthly_sales()
        observed_months, forecast_periods = seasonal_naive_forecast(
            monthly_result["data"], horizon
        )
    except ForecastUnavailable as exc:
        raise HTTPException(
            status_code=503,
            detail={
                "success": False,
                "status": "forecast_unavailable",
                "message": str(exc),
            },
        ) from exc
    except SnapshotUnavailable as exc:
        raise HTTPException(
            status_code=503,
            detail="The public analytics snapshot is unavailable or invalid.",
        ) from exc

    first, last = observed_months[0], observed_months[-1]
    forecast_start, forecast_end = forecast_periods[0], forecast_periods[-1]
    method = "seasonal_naive_12_month"
    return {
        "success": True,
        "question": question,
        "selected_action": method,
        "response": (
            f"Computed a {horizon}-month seasonal-naive baseline using each "
            "month's units from 12 months earlier. Historical observations are "
            f"separate ({first['year']}-{first['month']:02d} through "
            f"{last['year']}-{last['month']:02d}); forecast periods are "
            f"{forecast_start['year']}-{forecast_start['month']:02d} through "
            f"{forecast_end['year']}-{forecast_end['month']:02d}. This is an "
            "unbacktested baseline; no forecast accuracy or model superiority is claimed. "
            "Sales are units sold, not revenue or currency, and snapshot freshness is unverified."
        ),
        "method": method,
        "horizon": horizon,
        "observed_period": {
            "start": {"year": first["year"], "month": first["month"]},
            "end": {"year": last["year"], "month": last["month"]},
            "count": len(observed_months),
        },
        "observed_months": observed_months,
        "forecast_periods": forecast_periods,
        **{key: monthly_result[key] for key in (
            "data_source", "freshness_verified", "snapshot_generation", "units"
        )},
    }


@app.get("/forecast/predictions")
def forecast_predictions(horizon: int = Query(default=3, ge=1, le=12)):
    repository = analytics_repository()
    result = _compute_forecast("Computed public baseline forecast", horizon, repository)
    return {
        "success": True,
        "mode": "public_demo",
        "message": result["response"],
        "data": result["forecast_periods"],
        "method": result["method"],
        "horizon": result["horizon"],
        "data_source": result["data_source"],
        "freshness_verified": result["freshness_verified"],
        "snapshot_generation": result["snapshot_generation"],
        "units": result["units"],
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
    repository = analytics_repository()
    route = route_question(request.question)
    if route.intent is None:
        return {
            "success": False,
            "question": request.question,
            "selected_agents": ["Deterministic Analytics Router"],
            "response": f"{route.reason} Snapshot freshness against MySQL is unverified.",
            "supported": False,
            "answer_generated": False,
            "intent_status": route.status,
            **repository.metadata,
        }

    try:
        result = _execute_routed_question(route, request.question, repository)
    except HTTPException:
        raise
    except SnapshotUnavailable as exc:
        raise HTTPException(
            status_code=503,
            detail="The public analytics snapshot is unavailable or invalid.",
        ) from exc

    payload = {
        "success": True,
        "question": request.question,
        "selected_agents": ["Deterministic Analytics Router"],
        "response": _format_chat_answer(route, result["data"]),
        "supported": True,
        "answer_generated": True,
        "intent_status": "supported",
        "intent": route.intent,
        "data": result["data"],
        **{key: result[key] for key in (
            "data_source", "freshness_verified", "snapshot_generation", "units"
        )},
    }
    if route.intent == "forecast_baseline":
        payload.update({
            "method": result["method"],
            "horizon": result["horizon"],
            "forecast_periods": result["forecast_periods"],
            "observed_period": result["observed_period"],
        })
    return payload


def _format_chat_answer(route: ChatRoute, rows: list[dict[str, Any]]) -> str:
    """Render a concise response using only rows returned by repository calls."""
    if route.intent == "forecast_baseline":
        periods = "; ".join(
            f"{row['year']}-{row['month']:02d}: {row['predicted_units']:,} units"
            for row in rows
        )
        return (
            f"Computed a {route.horizon}-month seasonal-naive baseline using the read-only monthly snapshot. "
            f"Forecast values: {periods}. This baseline repeats units from 12 months earlier; "
            "it is not a trained model and has not been backtested. Sales are units sold, not revenue or currency. "
            "Snapshot freshness against MySQL is unverified."
        )
    if route.intent == "summary":
        row = rows[0]
        content = (
            f"The aggregate snapshot contains **{row['total_records']:,} daily item-store fact rows** "
            f"and **{row['total_sales']:,} units sold**. Average: "
            f"{row['average_sales']:.4f} units per fact row; minimum: "
            f"{row['minimum_sales']:,}; maximum: {row['maximum_sales']:,}."
        )
    elif route.intent == "monthly_sales":
        if not rows:
            content = "No monthly aggregate rows are available in this snapshot."
        else:
            first, last = rows[0], rows[-1]
            peak = max(rows, key=lambda row: row["total_sales"])
            trough = min(rows, key=lambda row: row["total_sales"])
            first_period = f"{first['year']}-{first['month']:02d}"
            last_period = f"{last['year']}-{last['month']:02d}"
            change = last["total_sales"] - first["total_sales"]
            direction = "increase" if change > 0 else "decrease" if change < 0 else "no change"
            content = (
                f"The snapshot has **{len(rows)} monthly points**, from {first_period} to {last_period}. "
                f"Units changed from {first['total_sales']:,} to {last['total_sales']:,} "
                f"({direction} of {abs(change):,} units). Highest month: "
                f"{peak['year']}-{peak['month']:02d} ({peak['total_sales']:,} units); "
                f"lowest: {trough['year']}-{trough['month']:02d} ({trough['total_sales']:,} units)."
            )
    elif route.intent in {"top_stores", "top_products"}:
        noun, key = ("store", "store_id") if route.intent == "top_stores" else ("product", "item_id")
        if rows:
            ranking = "\n".join(
                f"{index}. {row[key]} — {row['total_sales']:,} units"
                for index, row in enumerate(rows, start=1)
            )
            content = f"Top {noun}s by total units sold in the snapshot (up to {route.limit} rows):\n\n{ranking}"
        else:
            content = f"No {noun} ranking rows are available in this snapshot."
    else:
        labels = {
            "category_performance": ("Category", "cat_id"),
            "department_performance": ("Department", "dept_id"),
            "weekday_performance": ("Weekday", "weekday"),
        }
        label, key = labels[route.intent]
        ranking = "\n".join(
            f"- {row[key]}: {row['total_sales']:,} units"
            for row in rows
        )
        content = f"{label} performance by units sold in the snapshot:\n\n{ranking}"

    return (
        f"{content}\n\n"
        "This deterministic demo answer uses approved read-only aggregate data; it does not call Gemini. "
        "Sales are units sold, not currency. Store, product, category, department, and weekday aggregates "
        "do not provide a specific date range, so no period is inferred for those results. "
        "Snapshot freshness against MySQL is unverified."
    )


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
