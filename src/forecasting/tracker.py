import json

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
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        parameters = experiment.parameters

        if not isinstance(parameters, dict):
            parameters = {}

        parameters_json = json.dumps(
            parameters,
            default=str
        )

        values = (
            experiment.model_name,
            parameters_json,
            experiment.mae,
            experiment.rmse,
            experiment.mape,
            experiment.train_time,
            experiment.predict_time,
        )

        db.execute(query, values)
        db.commit()
        db.close()