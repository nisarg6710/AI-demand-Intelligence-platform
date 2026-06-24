import mysql.connector
from pathlib import Path
import yaml


class DatabaseConnection:

    @staticmethod
    def connect():

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",
            database="demand_intelligence"
        )

        return connection