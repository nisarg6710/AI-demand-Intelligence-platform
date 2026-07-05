from src.forecasting.pipeline import ForecastPipeline

from src.forecasting.prophet import ProphetModel


if __name__ == "__main__":

    ForecastPipeline.run(

        ProphetModel()
    )