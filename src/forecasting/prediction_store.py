from src.database.db_manager import DatabaseManager


class PredictionStore:

    @staticmethod
    def save(model_name, dates, actual, prediction):

        db = DatabaseManager()

        query = """
        INSERT INTO forecast_predictions
        (
            model_name,
            forecast_date,
            actual,
            prediction
        )
        VALUES (%s,%s,%s,%s)
        """

        rows = list(
            zip(
                [model_name] * len(dates),
                dates,
                actual,
                prediction
            )
        )

        db.executemany(query, rows)

        db.commit()
        db.close()