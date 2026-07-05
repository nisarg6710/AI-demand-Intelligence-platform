import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)


class ForecastMetrics:

    @staticmethod
    def mae(actual, predicted):

        return mean_absolute_error(
            actual,
            predicted
        )
    
    @staticmethod
    def rmse(actual, predicted):

        return np.sqrt(
            mean_squared_error(
                actual,
                predicted
            )
        )
    
    @staticmethod
    def mape(actual, predicted):

        actual, predicted = np.array(actual), np.array(predicted)

        return np.mean(
            np.abs(
                (actual - predicted)/actual
            )
        ) * 100