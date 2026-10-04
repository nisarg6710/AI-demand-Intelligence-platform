from dataclasses import dataclass

from src.forecasting.evaluator import ForecastEvaluator


@dataclass
class ModelMonitoringReport:
    mae: float
    rmse: float
    mape: float
    passed: bool
    alerts: list[str]


class ModelMonitor:
    """
    Monitors forecasting model performance against configurable
    metric thresholds.
    """

    def __init__(
        self,
        mae_threshold: float | None = None,
        rmse_threshold: float | None = None,
        mape_threshold: float | None = None,
    ):
        self.mae_threshold = mae_threshold
        self.rmse_threshold = rmse_threshold
        self.mape_threshold = mape_threshold

    def evaluate(self, actual, predicted) -> ModelMonitoringReport:

        metrics = ForecastEvaluator.evaluate(
            actual,
            predicted,
        )

        alerts = []

        mae = float(metrics["MAE"])
        rmse = float(metrics["RMSE"])
        mape = float(metrics["MAPE"])

        if (
            self.mae_threshold is not None
            and mae > self.mae_threshold
        ):
            alerts.append(
                f"MAE exceeded threshold: {mae:.4f} > "
                f"{self.mae_threshold:.4f}"
            )

        if (
            self.rmse_threshold is not None
            and rmse > self.rmse_threshold
        ):
            alerts.append(
                f"RMSE exceeded threshold: {rmse:.4f} > "
                f"{self.rmse_threshold:.4f}"
            )

        if (
            self.mape_threshold is not None
            and mape > self.mape_threshold
        ):
            alerts.append(
                f"MAPE exceeded threshold: {mape:.4f} > "
                f"{self.mape_threshold:.4f}"
            )

        return ModelMonitoringReport(
            mae=mae,
            rmse=rmse,
            mape=mape,
            passed=len(alerts) == 0,
            alerts=alerts,
        )