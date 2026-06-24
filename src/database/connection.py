import mysql.connector
from pathlib import Path
import yaml


class DatabaseConnection:

    @staticmethod
    def connect():

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="N96sarg@6710",
            database="demand_intelligence"
        )

        return connection