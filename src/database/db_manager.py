from src.database.connection import DatabaseConnection

class DatabaseManager:

    def __init__(self):
        self.connection = DatabaseConnection.connect()
        self.cursor = self.connection.cursor()

    
    def execute(self, query, values=None):

        if values:
            self.cursor.execute(query, values)
        
        else:
            self.cursor.execute(query)
    

    def executemany(self, query, values):
        self.cursor.executemany(query, values)

    
    def commit(self):
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()

    def fetchall(self):
        return self.cursor.fetchall()


    def fetchone(self):
        return self.cursor.fetchone()


    def columns(self):
        return [column[0] for column in self.cursor.description]
    
    def fetch_dataframe(self):

        import pandas as pd

        rows = self.fetchall()

        cols = self.columns()

        return pd.DataFrame(rows, columns=cols)