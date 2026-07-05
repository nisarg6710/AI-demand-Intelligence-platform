from src.forecasting.data import ForecastDataLoader

import time
from src.forecasting.result import ForecastResult

from src.forecasting.evaluator import ForecastEvaluator

from src.forecasting.visualizer import ForecastVisualizer

from src.forecasting.experiment import ForecastingExperiment

from src.forecasting.tracker import ExperimentTracker

from src.forecasting.prediction_store import PredictionStore


class ForecastPipeline:

    @staticmethod
    def run(model):

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

            model_name=model.name,

            mae=metrics["MAE"],

            rmse=metrics["RMSE"],

            mape=metrics["MAPE"],

            train_time=train_end - train_start,

            predict_time=predict_end - predict_start,
        )

        experiment = ForecastingExperiment(
            model_name=result.model_name,
            parameters=model.get_params() if hasattr(model, 'get_params') else {},
            mae = result.mae,
            rmse=result.rmse,
            mape=result.mape,
            train_time=result.train_time,
            predict_time=result.predict_time
        )

        ExperimentTracker.save(experiment)

        PredictionStore.save(
            result.model_name,
            test['date'],
            test['sales'],
            predictions
        )


        print(result)

        ForecastVisualizer.plot(
            train,
            test,
            predictions
        )

        return result
    

    def __str__(self):

        return f"""
    ========== Forecast Result ==========
    Model          : {self.model_name}

    MAE            : {self.mae:.2f}
    RMSE           : {self.rmse:.2f}
    MAPE           : {self.mape:.2f}

    Training Time  : {self.train_time:.4f} sec
    Prediction Time: {self.predict_time:.4f} sec
    =====================================
    """