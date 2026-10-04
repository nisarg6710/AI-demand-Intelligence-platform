import pandas as pd

from src.monitoring.data_quality import DataQualityMonitor


def test_data_quality_passes_for_valid_data():

    df = pd.DataFrame(
        {
            "sales": [100, 200, 300],
            "price": [10, 20, 30],
        }
    )

    monitor = DataQualityMonitor(
        required_columns=["sales", "price"],
        non_negative_columns=["sales", "price"],
    )

    report = monitor.generate_report(df)

    assert report.row_count == 3
    assert report.duplicate_count == 0
    assert report.passed is True


def test_data_quality_detects_negative_values():

    df = pd.DataFrame(
        {
            "sales": [100, -20, 300],
        }
    )

    monitor = DataQualityMonitor(
        required_columns=["sales"],
        non_negative_columns=["sales"],
    )

    report = monitor.generate_report(df)

    assert report.passed is False
    assert report.negative_values["sales"] == 1