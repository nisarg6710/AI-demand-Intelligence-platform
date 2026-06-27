class DataValidator:

    @staticmethod
    def validate_columns(df, required_columns):

        missing_columns = [
            column 
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing Columns: {missing_columns}"
            )
    

    @staticmethod
    def validate_not_empty(df):

        if df.empty:
            raise ValueError(
                "DataFrame is empty."
            )
    
    @staticmethod
    def validate_nulls(df, columns):
        for column in columns:

            if df[column].isnull().any():

                raise ValueError(
                    f"Column '{column}' contains null values."
                )