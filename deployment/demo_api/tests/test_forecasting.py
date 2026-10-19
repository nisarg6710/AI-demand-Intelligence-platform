import pytest

from deployment.demo_api.forecasting import (
    DEFAULT_FORECAST_HORIZON,
    MAX_FORECAST_HORIZON,
    ForecastUnavailable,
    seasonal_naive_forecast,
)


def known_monthly_rows():
    return [
        {"year": year, "month": month, "total_sales": month + (year - 2020) * 100}
        for year in (2020, 2021)
        for month in range(1, 13)
    ]


def test_seasonal_naive_calculation_matches_known_monthly_fixture():
    observed, forecast = seasonal_naive_forecast(known_monthly_rows(), horizon=3)
    assert len(observed) == 24
    assert observed[-1] == {"year": 2021, "month": 12, "actual_units": 112}
    assert forecast == [
        {"year": 2022, "month": 1, "predicted_units": 101},
        {"year": 2022, "month": 2, "predicted_units": 102},
        {"year": 2022, "month": 3, "predicted_units": 103},
    ]


def test_default_and_maximum_horizons():
    assert DEFAULT_FORECAST_HORIZON == 3
    _, default_forecast = seasonal_naive_forecast(known_monthly_rows())
    assert len(default_forecast) == DEFAULT_FORECAST_HORIZON
    _, max_forecast = seasonal_naive_forecast(known_monthly_rows(), MAX_FORECAST_HORIZON)
    assert len(max_forecast) == MAX_FORECAST_HORIZON
    assert max_forecast[-1] == {"year": 2022, "month": 12, "predicted_units": 112}


@pytest.mark.parametrize("horizon", [0, 13, True, "3"])
def test_forecast_helper_rejects_invalid_horizons(horizon):
    with pytest.raises(ForecastUnavailable, match="horizon"):
        seasonal_naive_forecast(known_monthly_rows(), horizon)


@pytest.mark.parametrize("rows, message", [
    (None, "unavailable or malformed"),
    ([], "At least 24"),
    (known_monthly_rows()[:23], "At least 24"),
    ([{"year": 2020, "month": 1}], "invalid schema"),
    ([{"year": 2020, "month": 1, "total_sales": float("nan")}] * 24, "invalid periods or units"),
])
def test_missing_malformed_or_insufficient_monthly_data_fails(rows, message):
    with pytest.raises(ForecastUnavailable, match=message):
        seasonal_naive_forecast(rows)


def test_irregular_or_unsorted_months_fail_without_fabricating_periods():
    rows = known_monthly_rows()
    del rows[5]
    with pytest.raises(ForecastUnavailable, match="consecutive"):
        seasonal_naive_forecast(rows)

    rows = known_monthly_rows()
    rows[0], rows[1] = rows[1], rows[0]
    with pytest.raises(ForecastUnavailable, match="consecutive"):
        seasonal_naive_forecast(rows)
