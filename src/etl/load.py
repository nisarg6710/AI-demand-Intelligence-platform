from src.database.connection import DatabaseConnection


def load_calendar(df):

    conn = DatabaseConnection.connect()

    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO calendar_dim
    (
        d,
        date,
        wm_yr_wk,
        weekday,
        wday,
        month,
        year,
        event_name_1,
        event_type_1,
        event_name_2,
        event_type_2,
        snap_CA,
        snap_TX,
        snap_WI
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for row in df.itertuples(index=False):

        cursor.execute(query, tuple(row))

    conn.commit()

    cursor.close()
    conn.close()