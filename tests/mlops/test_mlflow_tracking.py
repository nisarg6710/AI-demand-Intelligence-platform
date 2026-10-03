from pathlib import Path

from src.mlops.mlflow_tracking import MLflowTracker


def test_mlflow_tracker():

    tracker = MLflowTracker(
        experiment_name="test-demand-intelligence"
    )

    with tracker.start_run(
        run_name="mlflow-test-run"
    ):

        tracker.log_params(
            {
                "model": "test_model",
                "forecast_horizon": 12,
            }
        )

        tracker.log_metrics(
            {
                "mae": 10.5,
                "rmse": 15.2,
                "mape": 4.7,
            }
        )

        tracker.log_tags(
            {
                "project": "AI Demand Intelligence Platform",
                "stage": "milestone_12",
            }
        )

        run_id = tracker.get_active_run_id()

        assert run_id is not None

