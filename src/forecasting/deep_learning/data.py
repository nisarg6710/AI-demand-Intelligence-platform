import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from src.database.connection import DatabaseConnection


class ForecastDataLoader:
    """
    Loads and preprocesses data for DL forecasting models.
    """

    def __init__(
            self,
            train_ratio=0.70,
            validation_ratio=0.15
    ):
        self.train_ratio = train_ratio
        self.validation_ratio = validation_ratio
        self.scaler = MinMaxScaler()
    
    def load_data(self):
        connection = DatabaseConnection.connect()
        query = """
        SELECT
            date,
            SUM(sales) AS total_sales

        FROM sales_enriched
        GROUP BY date
        ORDER BY date        
        """
        df = pd.read_sql(query, connection)

        connection.close()

        df['date'] = pd.to_datetime(df['date'])

        return df

    def split_data(self, df):
        n = len(df)

        train_end = int(n * self.train_ratio)

        validation_end = int(
            n * (
                self.train_ratio +
                self.validation_ratio
            )
        )

        train = df.iloc[:train_end]

        validation = df.iloc[
            train_end:validation_end
        ]

        test = df.iloc[validation_end:]

        return train, validation, test
    
    def normalize(
            self,
            train,
            validation,
            test
    ):
        train_values = train[['total_sales']]
        validation_values = validation[['total_sales']]
        test_values = test[['total_sales']]

        ##fit only on training
        self.scaler.fit(train_values)

        ## transform
        train_scaled = self.scaler.transform(train_values)
        validation_scaled = self.scaler.transform(validation_values)
        test_scaled = self.scaler.transform(test_values)

        return (
            train_scaled,
            validation_scaled,
            test_scaled
        )
    
    def prepare(self):
        df = self.load_data()

        train, validation, test = self.split_data(df)

        train_scaled, validation_scaled, test_scaled = self.normalize(
            train,
            validation,
            test
        )

        return (
            train_scaled,
            validation_scaled,
            test_scaled,
            self.scaler
        )