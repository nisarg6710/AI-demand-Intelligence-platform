from src.etl.extract import extract_csv
from src.etl.pipeline import ETLPipeline
from src.etl.load import ETLLoader
from src.etl.config import ETLConfig

from src.transforms.dimensions import (
    transform_item_dimension,
    transform_store_dimension,
)

item_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_item_dimension,

    source_path="data/raw/m5/sales_train_validation.csv",

    target_table="item_dim",

    required_columns=[
        "item_id",
        "dept_id",
        "cat_id",
    ],

    null_check_columns=[
        "item_id",
        "dept_id",
        "cat_id",
    ],
)

store_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_store_dimension,

    source_path="data/raw/m5/sales_train_validation.csv",

    target_table="store_dim",

    required_columns=[
        "store_id",
        "state_id",
    ],

    null_check_columns=[
        "store_id",
        "state_id",
    ],
)

def run_dimension_pipeline():

    ETLPipeline.run(
        item_config,
        ETLLoader,
    )

    ETLPipeline.run(
        store_config,
        ETLLoader,
    )