from src.database.db_manager import DatabaseManager


class ETLLoader:

    @staticmethod
    def load_dataframe(df, table_name):
        db = DatabaseManager()

        columns = ", ".join(df.columns)

        placeholders = ", ".join(["%s"] * len(df.columns))

        query = f"""
        INSERT IGNORE INTO {table_name}
        ({columns})
        VALUES({placeholders})        
        """

        values = [
            tuple(row)
            for row in df.itertuples(index=False, name=None)
        ]

        db.executemany(query, values)

        db.commit()

        db.close()

        print(f"{len(values)} rows loaded into {table_name}")