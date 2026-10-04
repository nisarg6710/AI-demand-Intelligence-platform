import numpy as np
import pytest

from src.monitoring.drift import DriftMonitor


def test_drift_not_detected():

    reference = np.array(
        [10, 11, 12, 13, 14]
    )

    current = np.array(
        [10, 11, 12, 13, 14]
    )

    monitor = DriftMonitor(
        threshold=0.2
    )

    report = monitor.detect(
        reference,
        current,
    )

    assert report.drift_detected is False


def test_drift_detected():

    reference = np.array(
        [10, 11, 12, 13, 14]
    )

    current = np.array(
        [100, 110, 120, 130, 140]
    )

    monitor = DriftMonitor(
        threshold=0.2
    )

    report = monitor.detect(
        reference,
        current,
    )

    assert report.drift_detected is True


def test_empty_data_raises_error():

    monitor = DriftMonitor()

    with pytest.raises(ValueError):
        monitor.detect([], [1, 2, 3])