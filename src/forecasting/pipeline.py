import time

from src.forecasting.data import ForecastDataLoader
from src.forecasting.result import ForecastResult
from src.forecasting.evaluator import ForecastEvaluator
from src.forecasting.visualizer import ForecastVisualizer
from src.forecasting.experiment import ForecastingExperiment
from src.forecasting.tracker import ExperimentTracker
from src.forecasting.prediction_store import PredictionStore
from src.mlops.mlflow_tracking import MLflowTracker


class ForecastPipeline:

    @staticmethod
    def run(model):

        model_name = model.name

        mlflow_tracker = MLflowTracker(
            experiment_name="AI-Demand-Intelligence-Forecasting"
        )

        with mlflow_tracker.start_run(
            run_name=model_name
        ):

            print("Loading data...")

            df = ForecastDataLoader.load_daily_sales()

            print("Data loaded.")

            train, test = ForecastDataLoader.train_test_split(df)

            print("Data split.")

            train_start = time.perf_counter()

            model.fit(train)

            train_end = time.perf_counter()

            print("Model trained.")

            predict_start = time.perf_counter()

            predictions = model.predict(
                len(test)
            )

            predict_end = time.perf_counter()

            print("Predictions completed.")

            metrics = ForecastEvaluator.evaluate(
                test["sales"],
                predictions
            )

            result = ForecastResult(

                model_name=model_name,

                mae=metrics["MAE"],

                rmse=metrics["RMSE"],

                mape=metrics["MAPE"],

                train_time=train_end - train_start,

                predict_time=predict_end - predict_start,
            )

            parameters = {}

            if hasattr(model, "window"):
                parameters["window"] = model.window

            if hasattr(model, "order"):
                parameters["order"] = str(model.order)

            if hasattr(model, "seasonal_order"):
                parameters["seasonal_order"] = str(
                    model.seasonal_order
                )

            if hasattr(model, "trend"):
                parameters["trend"] = model.trend

            experiment = ForecastingExperiment(
                model_name=result.model_name,
                parameters=parameters,
                mae=result.mae,
                rmse=result.rmse,
                mape=result.mape,
                train_time=result.train_time,
                predict_time=result.predict_time
            )

            # Existing MySQL experiment tracking
            ExperimentTracker.save(experiment)

            # Existing prediction storage
            PredictionStore.save(
                result.model_name,
                test["date"],
                test["sales"],
                predictions
            )

            # MLflow parameters
            mlflow_tracker.log_params({
                "model_name": result.model_name,
                "model_family": "classical",
                "forecast_horizon": len(test),
                **parameters,
            })

            # MLflow metrics
            mlflow_tracker.log_metrics({
                "MAE": result.mae,
                "RMSE": result.rmse,
                "MAPE": result.mape,
                "train_time": result.train_time,
                "predict_time": result.predict_time,
            })

            # MLflow tags
            mlflow_tracker.log_tags({
                "project": "AI-Demand-Intelligence-Platform",
                "stage": "forecasting",
                "model_family": "classical",
                "model_name": result.model_name,
            })

            # Generate forecast artifact
            forecast_plot = ForecastVisualizer.plot(
                train,
                test,
                predictions,
                result.model_name,
            )

            # Log forecast plot to MLflow
            mlflow_tracker.log_artifact(
                forecast_plot,
                artifact_path="forecasts",
            )

            print(result)

            return result


## mlflow run command:--> "python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000 --workers 1"