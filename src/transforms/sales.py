import pandas as pd

def transform_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the M5 sales dataset from wide format to long format.

    Input:
        item_id | store_id | d_1 | d_2 | ...

    Output:
        item_id | store_id | d | sales
    """

    id_columns = [
        'item_id',
        'store_id'
    ]

    day_columns = [
        column
        for column in df.columns
        if column.startswith('d_')
    ]

    sales_df = pd.melt(
        df,
        id_vars=id_columns,
        value_vars=day_columns,
        var_name='d',
        value_name='sales'
    )

    return sales_df