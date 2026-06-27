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

    