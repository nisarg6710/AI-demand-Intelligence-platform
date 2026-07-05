import numpy as np

from src.forecasting.base import ForecastModel


class MovingAverageModel(ForecastModel):

    def __init__(self, window=7):

        self.window = window
        self.train = None

    def fit(self, train_df):

        self.train = train_df.copy()

    def predict(self, horizon):

        predictions = []

        history = self.train["sales"].tolist()

        for _ in range(horizon):

            prediction = np.mean(
                history[-self.window:]
            )

            predictions.append(prediction)

            history.append(prediction)

        return predictions