from src.database.db_manager import DatabaseManager


class ExperimentTracker:

    @staticmethod
    def save(experiment):

        db = DatabaseManager()

        query = """
        INSERT INTO forecast_experiments
        (
            model_name,
            parameters,
            mae,
            rmse,
            mape,
            train_time,
            predict_time
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            experiment.model_name,
            str(experiment.parameters),
            experiment.mae,
            experiment.rmse,
            experiment.mape,
            experiment.train_time,
            experiment.predict_time,
        )

        db.execute(query, values)
        db.commit()
        db.close()