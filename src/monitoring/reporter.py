import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from src.mlops.mlflow_tracking import MLflowTracker
from src.monitoring.data_quality import DataQualityMonitor
from src.monitoring.drift import DriftMonitor
from src.monitoring.model_monitor import ModelMonitor


class MonitoringReporter:
    """
    Orchestrates data-quality, model-performance, and drift monitoring.

    The reporter creates a single structured monitoring report and can
    optionally log the report to MLflow.
    """

    def __init__(
        self,
        output_directory: str | Path = "artifacts/monitoring",
    ):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate_report(
        self,
        *,
        data=None,
        actual=None,
        predicted=None,
        reference=None,
        current=None,
        data_monitor: DataQualityMonitor | None = None,
        model_monitor: ModelMonitor | None = None,
        drift_monitor: DriftMonitor | None = None,
    ) -> dict[str, Any]:

        report = {
            "timestamp": datetime.now().isoformat(),
            "status": "healthy",
        }

        # -----------------------------------------------------
        # Data quality
        # -----------------------------------------------------

        if data is not None:

            if data_monitor is None:
                data_monitor = DataQualityMonitor()

            data_quality = data_monitor.generate_report(data)

            report["data_quality"] = asdict(data_quality)

        # -----------------------------------------------------
        # Model performance
        # -----------------------------------------------------

        if actual is not None and predicted is not None:

            if model_monitor is None:
                model_monitor = ModelMonitor()

            model_report = model_monitor.evaluate(
                actual,
                predicted,
            )

            report["model_performance"] = asdict(
                model_report
            )

        # -----------------------------------------------------
        # Drift
        # -----------------------------------------------------

        if reference is not None and current is not None:

            if drift_monitor is None:
                drift_monitor = DriftMonitor()

            drift_report = drift_monitor.detect(
                reference,
                current,
            )

            report["drift"] = asdict(
                drift_report
            )

        # -----------------------------------------------------
        # Overall status
        # -----------------------------------------------------

        if (
            report.get("data_quality", {}).get("passed") is False
            or report.get("model_performance", {}).get("passed") is False
            or report.get("drift", {}).get("drift_detected") is True
        ):
            report["status"] = "warning"

        return report

    def save_report(
        self,
        report: dict[str, Any],
        filename: str = "monitoring_report.json",
    ) -> Path:

        output_path = self.output_directory / filename

        with output_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                default=str,
            )

        return output_path

    def log_to_mlflow(
        self,
        report: dict[str, Any],
        tracker: MLflowTracker | None = None,
    ):

        if tracker is None:
            tracker = MLflowTracker()

        with tracker.start_run(
            run_name="monitoring-run",
            tags={
                "project": "AI Demand Intelligence Platform",
                "stage": "monitoring",
            },
        ):

            status = report.get(
                "status",
                "unknown",
            )

            tracker.log_tags(
                {
                    "monitoring_status": status,
                }
            )

            model_metrics = report.get(
                "model_performance",
                {},
            )

            if model_metrics:

                tracker.log_metrics(
                    {
                        "monitoring_mae": model_metrics.get(
                            "mae"
                        ),
                        "monitoring_rmse": model_metrics.get(
                            "rmse"
                        ),
                        "monitoring_mape": model_metrics.get(
                            "mape"
                        ),
                    }
                )

            drift = report.get(
                "drift",
                {},
            )

            if drift:

                tracker.log_metrics(
                    {
                        "drift_statistic": drift.get(
                            "statistic"
                        ),
                    }
                )

            report_path = self.save_report(
                report,
                "monitoring_report.json",
            )

            tracker.log_artifact(
                report_path,
                artifact_path="monitoring",
            )

            return tracker.get_active_run_id()