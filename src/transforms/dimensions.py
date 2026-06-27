import pandas as pd



def transform_item_dimension(df):

    item_df = (
        df[
            [
                'item_id',
                'dept_id',
                'cat_id'
            ]
        ]
        .drop_duplicates()
        .sort_values('item_id')
        .reset_index(drop=True)
    )

    return item_df


def transform_store_dimension(df):

    item_df = (
        df[
            [
                'store_id',
                'state_id'
            ]
        ]
        .drop_duplicates()
        .sort_values('store_id')
        .reset_index(drop=True)
    )

    return item_df