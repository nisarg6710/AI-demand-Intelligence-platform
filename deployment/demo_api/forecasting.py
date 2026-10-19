"""Small, deterministic forecasting helpers for monthly aggregate snapshots."""

from __future__ import annotations

import math
from typing import Any


SEASONAL_PERIOD_MONTHS = 12
MINIMUM_HISTORY_MONTHS = 24
MAX_FORECAST_HORIZON = 12
DEFAULT_FORECAST_HORIZON = 3


class ForecastUnavailable(ValueError):
    """The monthly snapshot cannot safely support the selected baseline."""


def _period_index(year: int, month: int) -> int:
    return year * 12 + month - 1


def _period_from_index(index: int) -> tuple[int, int]:
    year, month_zero_based = divmod(index, 12)
    return year, month_zero_based + 1


def seasonal_naive_forecast(
    monthly_rows: Any,
    horizon: int = DEFAULT_FORECAST_HORIZON,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return separate observed and forecast periods using a 12-month lag.

    The input must be a chronologically ordered, complete monthly calendar with
    at least two annual cycles. The method repeats the observed value from the
    same calendar month in the previous year; it makes no accuracy claim.
    """
    if type(horizon) is not int or not 1 <= horizon <= MAX_FORECAST_HORIZON:
        raise ForecastUnavailable(
            f"Forecast horizon must be an integer from 1 to {MAX_FORECAST_HORIZON} months"
        )
    if not isinstance(monthly_rows, list):
        raise ForecastUnavailable("Monthly aggregate data is unavailable or malformed")
    observed: list[dict[str, Any]] = []
    previous_index: int | None = None
    for row in monthly_rows:
        if not isinstance(row, dict) or not {"year", "month", "total_sales"}.issubset(row):
            raise ForecastUnavailable("Monthly aggregate rows have an invalid schema")
        year, month, units = row["year"], row["month"], row["total_sales"]
        if (
            type(year) is not int
            or not 1 <= year <= 9999
            or type(month) is not int
            or not 1 <= month <= 12
            or type(units) not in (int, float)
            or (type(units) is float and not math.isfinite(units))
            or units < 0
        ):
            raise ForecastUnavailable("Monthly aggregate rows contain invalid periods or units")
        current_index = _period_index(year, month)
        if previous_index is not None and current_index != previous_index + 1:
            raise ForecastUnavailable(
                "Monthly aggregate periods must be unique, ordered, and consecutive"
            )
        observed.append({"year": year, "month": month, "actual_units": units})
        previous_index = current_index

    if len(observed) < MINIMUM_HISTORY_MONTHS:
        raise ForecastUnavailable(
            f"At least {MINIMUM_HISTORY_MONTHS} complete monthly observations are required"
        )

    forecast: list[dict[str, Any]] = []
    last_index = _period_index(observed[-1]["year"], observed[-1]["month"])
    for step in range(1, horizon + 1):
        target_index = last_index + step
        year, month = _period_from_index(target_index)
        if year > 9999:
            raise ForecastUnavailable("Forecast period exceeds the supported calendar range")
        source = observed[-SEASONAL_PERIOD_MONTHS + ((step - 1) % SEASONAL_PERIOD_MONTHS)]
        forecast.append({
            "year": year,
            "month": month,
            "predicted_units": source["actual_units"],
        })
    return observed, forecast
