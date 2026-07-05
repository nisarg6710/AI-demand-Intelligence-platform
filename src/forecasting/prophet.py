from prophet import Prophet

from src.forecasting.base import ForecastModel


class ProphetModel(ForecastModel):

    def __init__(self):

        self.model = Prophet(

            yearly_seasonality=True,

            weekly_seasonality=True,

            daily_seasonality=False,
        )

        self.forecast = None

    def fit(self, train_df):

        df = train_df.rename(

            columns={

                "date": "ds",

                "sales": "y",
            }
        )

        self.model.fit(df)

        self.train_size = len(df)

    def predict(self, horizon):

        future = self.model.make_future_dataframe(

            periods=horizon,

            freq="D",
        )

        forecast = self.model.predict(future)

        predictions = forecast["yhat"].tail(horizon)

        return predictions.tolist()