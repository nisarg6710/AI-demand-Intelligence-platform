# from src.database.connection import DatabaseConnection

## this was just an example now we'll make a generic dataframe loader here.
# def load_calendar(df):

#     conn = DatabaseConnection.connect()

#     cursor = conn.cursor()

#     query = """
#     INSERT IGNORE INTO calendar_dim
#     (
#         d,
#         date,
#         wm_yr_wk,
#         weekday,
#         wday,
#         month,
#         year,
#         event_name_1,
#         event_type_1,
#         event_name_2,
#         event_type_2,
#         snap_CA,
#         snap_TX,
#         snap_WI
#     )
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#     """

#     for row in df.itertuples(index=False): 

#         cursor.execute(query, tuple(row))

#     conn.commit()

#     cursor.close()
#     conn.close()
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