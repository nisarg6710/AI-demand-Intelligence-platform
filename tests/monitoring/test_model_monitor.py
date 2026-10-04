import numpy as np

from src.monitoring.model_monitor import ModelMonitor


def test_model_monitor_passes():

    actual = np.array([100, 200, 300])
    predicted = np.array([100, 200, 300])

    monitor = ModelMonitor(
        mae_threshold=1,
        rmse_threshold=1,
        mape_threshold=1,
    )

    report = monitor.evaluate(
        actual,
        predicted,
    )

    assert report.mae == 0
    assert report.rmse == 0
    assert report.mape == 0
    assert report.passed is True
    assert report.alerts == []


def test_model_monitor_detects_bad_model():

    actual = np.array([100, 200, 300])
    predicted = np.array([200, 400, 600])

    monitor = ModelMonitor(
        mae_threshold=10,
        rmse_threshold=10,
        mape_threshold=10,
    )

    report = monitor.evaluate(
        actual,
        predicted,
    )

    assert report.passed is False
    assert len(report.alerts) > 0