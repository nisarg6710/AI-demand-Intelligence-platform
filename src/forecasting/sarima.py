from statsmodels.tsa.statespace.sarimax import SARIMAX

from src.forecasting.base import ForecastModel


class SARIMAModel(ForecastModel):

    def __init__(
        self,
        order=(1, 1, 0),
        seasonal_order=(2, 0, 1, 7),
    ):

        self.order = order
        self.seasonal_order = seasonal_order

        self.model = None
        self.fitted_model = None

    def fit(self, train_df):

        self.model = SARIMAX(
            train_df["sales"],
            order=self.order,
            seasonal_order=self.seasonal_order,
            enforce_stationarity=False,
            enforce_invertibility=False,
        )

        self.fitted_model = self.model.fit(
            disp=False
        )

    def predict(self, horizon):

        forecast = self.fitted_model.forecast(
            steps=horizon
        )

        return forecast.tolist()