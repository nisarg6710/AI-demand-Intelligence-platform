import pandas as pd

def transform_calendar(df):

    df["date"] = pd.to_datetime(df["date"])

    df = df[
        [
            "d",
            "date",
            "wm_yr_wk",
            "weekday",
            "wday",
            "month",
            "year",
            "event_name_1",
            "event_type_1",
            "event_name_2",
            "event_type_2",
            "snap_CA",
            "snap_TX",
            "snap_WI"
        ]
    ]

    return df