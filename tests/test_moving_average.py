from src.forecasting.pipeline import ForecastPipeline

from src.forecasting.moving_average import MovingAverageModel

if __name__ == '__main__':
    model = MovingAverageModel(window=7)

    ForecastPipeline.run(model)