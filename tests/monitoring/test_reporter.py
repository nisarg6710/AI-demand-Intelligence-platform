import json

import numpy as np
import pandas as pd

from src.monitoring.data_quality import DataQualityMonitor
from src.monitoring.drift import DriftMonitor
from src.monitoring.model_monitor import ModelMonitor
from src.monitoring.reporter import MonitoringReporter


def test_monitoring_report(tmp_path):

    data = pd.DataFrame(
        {
            "sales": [100, 200, 300],
            "price": [10, 20, 30],
        }
    )

    actual = np.array(
        [100, 200, 300]
    )

    predicted = np.array(
        [100, 200, 300]
    )

    reference = np.array(
        [10, 11, 12, 13, 14]
    )

    current = np.array(
        [10, 11, 12, 13, 14]
    )

    reporter = MonitoringReporter(
        output_directory=tmp_path
    )

    report = reporter.generate_report(
        data=data,
        actual=actual,
        predicted=predicted,
        reference=reference,
        current=current,
        data_monitor=DataQualityMonitor(
            required_columns=[
                "sales",
                "price",
            ],
            non_negative_columns=[
                "sales",
                "price",
            ],
        ),
        model_monitor=ModelMonitor(
            mae_threshold=1,
            rmse_threshold=1,
            mape_threshold=1,
        ),
        drift_monitor=DriftMonitor(
            threshold=0.2
        ),
    )

    assert report["status"] == "healthy"

    assert report["data_quality"]["passed"] is True

    assert report["model_performance"]["passed"] is True

    assert report["drift"]["drift_detected"] is False


def test_monitoring_report_detects_warning(tmp_path):

    data = pd.DataFrame(
        {
            "sales": [100, -200, 300],
        }
    )

    actual = np.array(
        [100, 200, 300]
    )

    predicted = np.array(
        [200, 400, 600]
    )

    reporter = MonitoringReporter(
        output_directory=tmp_path
    )

    report = reporter.generate_report(
        data=data,
        actual=actual,
        predicted=predicted,
        data_monitor=DataQualityMonitor(
            required_columns=["sales"],
            non_negative_columns=["sales"],
        ),
        model_monitor=ModelMonitor(
            mae_threshold=10,
            rmse_threshold=10,
            mape_threshold=10,
        ),
    )

    assert report["status"] == "warning"


def test_monitoring_report_can_be_saved(tmp_path):

    reporter = MonitoringReporter(
        output_directory=tmp_path
    )

    report = {
        "status": "healthy",
    }

    path = reporter.save_report(report)

    assert path.exists()

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:

        saved_report = json.load(file)

    assert saved_report["status"] == "healthy"