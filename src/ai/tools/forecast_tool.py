from src.ai.tools.base_tool import BaseTool
from src.database.db_manager import DatabaseManager


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
        """

        try:

            db = DatabaseManager()

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

            db.close()

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

        return self.failure(f"Unknown action: {action}")