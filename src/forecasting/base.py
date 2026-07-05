from abc import ABC, abstractmethod


## EVERY FORECASTING MODEL WILL INHERIT FROM THIS.

class ForecastModel(ABC):

    @property
    def name(self):
        return self.__class__.__name__

    @abstractmethod
    def fit(self, train_df):
        pass

    @abstractmethod
    def predict(self, horizon):
        pass
