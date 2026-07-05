from src.forecasting.arima import ARIMAModel

from src.forecasting.pipeline import ForecastPipeline

if __name__ == "__main__":
    model = ARIMAModel(
        order = (5,1,0)
    )

    ForecastPipeline.run(model)