from src.forecasting.pipeline import ForecastPipeline
from src.forecasting.sarima import SARIMAModel


if __name__ == "__main__":

    model = SARIMAModel()

    ForecastPipeline.run(model)