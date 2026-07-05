import pandas as pd

from src.database.connection import DatabaseConnection

class ForecastDataLoader:

    @staticmethod
    def load_daily_sales():
        connection = DatabaseConnection.connect()

        query = """
        SELECT
            date,
            SUM(sales) AS sales

        FROM sales_enriched
        GROUP BY date
        ORDER BY date        
        """

        df = pd.read_sql(query, connection)

        connection.close()

        df['date'] = pd.to_datetime(df['date'])

        return df


    @staticmethod
    def train_test_split(df, train_ratio=0.8):
        
        split_index = int(len(df) * train_ratio)

        train = df.iloc[:split_index].copy()

        test = df.iloc[split_index:].copy()

        return train, test