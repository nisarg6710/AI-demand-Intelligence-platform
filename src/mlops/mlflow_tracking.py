import os
from pathlib import Path
from typing import Any

import mlflow


class MLflowTracker:
    """
    Centralized MLflow experiment tracking utility.

    This class provides a reusable interface for:
    - Experiment creation
    - Run management
    - Parameter logging
    - Metric logging
    - Tag logging
    - Artifact logging
    - Model logging
    """

    def __init__(
        self,
        experiment_name: str = "AI-Demand-Intelligence-Forecasting",
        tracking_uri: str | None = None,
    ):
        """
        Initialize the MLflow tracker.

        Parameters
        ----------
        experiment_name:
            Name of the MLflow experiment.

        tracking_uri:
            MLflow tracking URI.

            If not provided, a local MLflow directory is used.
        """

        if tracking_uri is None:
            tracking_uri = os.getenv(
                "MLFLOW_TRACKING_URI",
                "sqlite:///mlflow.db",
            )

        mlflow.set_tracking_uri(tracking_uri)

        self.experiment_name = experiment_name

        mlflow.set_experiment(self.experiment_name)

    # ---------------------------------------------------------
    # Run Management
    # ---------------------------------------------------------

    def start_run(
        self,
        run_name: str | None = None,
        tags: dict[str, Any] | None = None,
    ):
        """
        Start an MLflow run.

        Returns
        -------
        Active MLflow run.
        """

        return mlflow.start_run(
            run_name=run_name,
            tags=tags,
        )

    def end_run(self):
        """End the currently active MLflow run."""

        if mlflow.active_run() is not None:
            mlflow.end_run()

    # ---------------------------------------------------------
    # Parameters
    # ---------------------------------------------------------

    def log_params(self, params: dict[str, Any]):
        """
        Log experiment parameters.

        Non-serializable values are converted to strings.
        """

        cleaned_params = {}

        for key, value in params.items():
            if value is None:
                continue

            if isinstance(value, (str, int, float, bool)):
                cleaned_params[key] = value
            else:
                cleaned_params[key] = str(value)

        if cleaned_params:
            mlflow.log_params(cleaned_params)

    # ---------------------------------------------------------
    # Metrics
    # ---------------------------------------------------------

    def log_metrics(self, metrics: dict[str, float]):
        """
        Log numerical evaluation metrics.
        """

        cleaned_metrics = {}

        for key, value in metrics.items():

            if value is None:
                continue

            try:
                cleaned_metrics[key] = float(value)
            except (TypeError, ValueError):
                continue

        if cleaned_metrics:
            mlflow.log_metrics(cleaned_metrics)

    # ---------------------------------------------------------
    # Tags
    # ---------------------------------------------------------

    def log_tags(self, tags: dict[str, Any]):
        """
        Log metadata tags for the current run.
        """

        cleaned_tags = {}

        for key, value in tags.items():

            if value is None:
                continue

            cleaned_tags[key] = str(value)

        if cleaned_tags:
            mlflow.set_tags(cleaned_tags)

    # ---------------------------------------------------------
    # Artifacts
    # ---------------------------------------------------------

    def log_artifact(
        self,
        file_path: str | Path,
        artifact_path: str | None = None,
    ):
        """
        Log a single artifact.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(
                f"Artifact does not exist: {file_path}"
            )

        mlflow.log_artifact(
            str(file_path),
            artifact_path=artifact_path,
        )

    def log_artifacts(
        self,
        directory: str | Path,
        artifact_path: str | None = None,
    ):
        """
        Log all files inside a directory.
        """

        directory = Path(directory)

        if not directory.exists():
            raise FileNotFoundError(
                f"Artifact directory does not exist: {directory}"
            )

        mlflow.log_artifacts(
            str(directory),
            artifact_path=artifact_path,
        )

    # ---------------------------------------------------------
    # Model
    # ---------------------------------------------------------

    def log_model(
        self,
        model,
        artifact_path: str = "model",
    ):
        """
        Log a generic MLflow model.

        This method is intentionally kept generic because
        forecasting models in this project use multiple
        frameworks.
        """

        return mlflow.pyfunc.log_model(
            artifact_path=artifact_path,
            python_model=model,
        )

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    @staticmethod
    def get_active_run_id() -> str | None:
        """
        Return the active MLflow run ID.
        """

        run = mlflow.active_run()

        if run is None:
            return None

        return run.info.run_id