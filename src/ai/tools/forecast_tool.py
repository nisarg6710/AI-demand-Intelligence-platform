from src.ai.tools.base_tool import BaseTool
from src.database.db_manager import DatabaseManager

import pandas as pd
from prophet import Prophet



class ForecastTool(BaseTool):

    @property
    def name(self):
        return "Accesses forecasting experiments and prediction results."

    @property
    def description(self):
        return "Runs demand forecasting models."


    def get_best_model(self):
        """
        Returns the best-performing forecasting model based on MAPE.
        """

        try:
            db = DatabaseManager()

            query = """
            SELECT
                model_name,
                mae,
                rmse,
                mape
            FROM forecast_experiments
            ORDER BY mape ASC
            LIMIT 1;
            """

            db.execute(query)

            df = db.fetch_dataframe()

            db.close()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns),
                    "query": query.strip(),
                },
            )

        except Exception as e:

            return self.failure(str(e))

    def compare_models(self):
        """
        Returns the performance metrics of all forecasting models.
        """

        try:

            db = DatabaseManager()

            query = """
            SELECT
                model_name,
                mae,
                rmse,
                mape
            FROM forecast_experiments
            ORDER BY mape ASC;
            """

            db.execute(query)

            df = db.fetch_dataframe()

            db.close()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns),
                    "query": query.strip(),
                },
            )

        except Exception as e:

            return self.failure(str(e))

    def get_predictions(self, model_name):
        """
        Returns stored predictions for a specific forecasting model.

        Supports the special model name 'best_model', which resolves
        automatically to the model with the lowest MAPE.
        """

        db = DatabaseManager()

        try:

            # --------------------------------------------------
            # Normalize model name
            # --------------------------------------------------

            normalized_model_name = (
                model_name
                .strip()
                .lower()
                .replace("-", "_")
                .replace(" ", "_")
            )

            # Handle:
            # best_model
            # bestmodel
            # BestModel
            # best-model
            if normalized_model_name in {
                "best_model",
                "bestmodel",
            }:

                best_model_query = """
                SELECT
                    model_name
                FROM forecast_experiments
                ORDER BY mape ASC
                LIMIT 1;
                """

                db.execute(best_model_query)

                best_model_df = db.fetch_dataframe()

                if best_model_df.empty:

                    return self.failure(
                        "No forecasting experiments are available."
                    )

                model_name = best_model_df.iloc[0]["model_name"]

            # --------------------------------------------------
            # Fetch predictions
            # --------------------------------------------------

            query = """
            SELECT
                forecast_date,
                actual,
                prediction
            FROM forecast_predictions
            WHERE model_name = %s
            ORDER BY forecast_date;
            """

            db.execute(query, (model_name,))

            df = db.fetch_dataframe()

            if df.empty:

                return self.failure(
                    f"No prediction data found for model '{model_name}'."
                )

            return self.success(
                data=df,
                metadata={
                    "model_name": model_name,
                    "rows": len(df),
                    "columns": list(df.columns),
                    "query": query.strip(),
                },
            )

        except Exception as e:

            return self.failure(str(e))

        finally:

            db.close()

    def get_experiments(self):
        """
        Returns all forecasting experiments.
        """

        try:

            db = DatabaseManager()

            query = """
            SELECT
                experiment_id,
                model_name,
                parameters,
                mae,
                rmse,
                mape,
                train_time,
                predict_time,
                created_at
            FROM forecast_experiments
            ORDER BY created_at DESC;
            """

            db.execute(query)

            df = db.fetch_dataframe()

            db.close()

            return self.success(
                data=df,
                metadata={
                    "rows": len(df),
                    "columns": list(df.columns),
                    "query": query.strip(),
                },
            )

        except Exception as e:

            return self.failure(str(e))

    def get_future_forecast(self, periods=12):
        """
        Generates future monthly demand forecasts using the
        best-performing forecasting model.

        Currently uses Prophet because it achieved the
        lowest MAPE in forecast_experiments.
        """

        db = None

        try:

            db = DatabaseManager()

            # --------------------------------------------------
            # Get historical monthly demand
            # --------------------------------------------------

            query = """
            SELECT
                year,
                month,
                total_sales
            FROM analytics_monthly_sales
            ORDER BY year, month;
            """

            db.execute(query)

            df = db.fetch_dataframe()

            if df.empty:

                return self.failure(
                    "No historical monthly sales data available."
                )

            # --------------------------------------------------
            # Prepare Prophet dataset
            # --------------------------------------------------

            df["ds"] = pd.to_datetime(
                df["year"].astype(str)
                + "-"
                + df["month"].astype(str)
                + "-01"
            )

            df["y"] = df["total_sales"].astype(float)

            prophet_df = df[["ds", "y"]].copy()

            # --------------------------------------------------
            # Train Prophet on historical monthly demand
            # --------------------------------------------------

            model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=False,
                daily_seasonality=False,
            )

            model.fit(prophet_df)

            # --------------------------------------------------
            # Generate future dates
            # --------------------------------------------------

            future = model.make_future_dataframe(
                periods=periods,
                freq="MS",
            )

            forecast = model.predict(future)

            # --------------------------------------------------
            # Keep only future predictions
            # --------------------------------------------------

            last_historical_date = prophet_df["ds"].max()

            future_forecast = forecast[
                forecast["ds"] > last_historical_date
            ][
                ["ds", "yhat", "yhat_lower", "yhat_upper"]
            ].copy()

            future_forecast.rename(
                columns={
                    "ds": "forecast_date",
                    "yhat": "prediction",
                    "yhat_lower": "lower_bound",
                    "yhat_upper": "upper_bound",
                },
                inplace=True,
            )

            future_forecast["prediction"] = (
                future_forecast["prediction"]
                .clip(lower=0)
            )

            return self.success(
                data=future_forecast,
                metadata={
                    "model_name": "ProphetModel",
                    "forecast_periods": periods,
                    "historical_start": str(
                        prophet_df["ds"].min().date()
                    ),
                    "historical_end": str(
                        prophet_df["ds"].max().date()
                    ),
                    "forecast_start": str(
                        future_forecast["forecast_date"]
                        .min()
                        .date()
                    ),
                    "forecast_end": str(
                        future_forecast["forecast_date"]
                        .max()
                        .date()
                    ),
                    "rows": len(future_forecast),
                },
            )

        except Exception as e:

            return self.failure(str(e))

        finally:

            if db:
                db.close()

    def execute(self, action, **kwargs):
        """
        Dispatches forecasting tool actions.
        """

        if action == "get_best_model":
            return self.get_best_model()

        elif action == "compare_models":
            return self.compare_models()

        elif action == "get_predictions":
            return self.get_predictions(kwargs["model_name"])

        elif action == "get_experiments":
            return self.get_experiments()

        elif action == "get_future_forecast":
            periods = kwargs.get("periods", 12)

            return self.get_future_forecast(periods)

        return self.failure(f"Unknown action: {action}")


