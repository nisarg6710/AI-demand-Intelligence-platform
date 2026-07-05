from statsmodels.tsa.arima.model import ARIMA

from src.forecasting.base import ForecastModel


class ARIMAModel(ForecastModel):

    def __init__(self, order=(5, 1, 0), trend='n'):

        self.order = order
        self.trend = trend
        self.model = None
        self.fitted_model = None

    def fit(self, train_df):

        self.model = ARIMA(
            train_df["sales"],
            order=self.order,
            trend=self.trend
        )

        self.fitted_model = self.model.fit()

    def predict(self, horizon):

        forecast = self.fitted_model.forecast(
            steps=horizon
        )

        return forecast.tolist()