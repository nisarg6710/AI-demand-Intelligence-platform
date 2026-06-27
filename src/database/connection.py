import mysql.connector

from src.config.settings import Settings


class DatabaseConnection:

    @staticmethod
    def connect():

        db = Settings.database["database"]

        return mysql.connector.connect(
            host=db["host"],
            user=db["user"],
            password=db["password"],
            database=db["database"]
        )