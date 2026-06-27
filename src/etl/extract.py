import pandas as pd


def extract_csv(path, chunksize=None):

    return pd.read_csv(
        path,
        chunksize=chunksize
    )


def extract_calendar(path: str, chunksize=None):
    return extract_csv(path, chunksize=chunksize)