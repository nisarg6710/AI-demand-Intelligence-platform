from src.etl.extract import extract_csv
from src.etl.transform import (
    transform_item_dimension,
    transform_store_dimension
)

from src.etl.load import ETLLoader


sales = extract_csv(
    'data/raw/m5/sales_train_validation.csv'
)

item_df = transform_item_dimension(sales)

store_df = transform_store_dimension(sales)

ETLLoader.load_dataframe(
    item_df,
    'item_dim'
)

ETLLoader.load_dataframe(
    store_df,
    'store_dim'
)

print("Dimensions table loaded successfully.")
