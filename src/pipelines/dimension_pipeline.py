from src.etl.extract import extract_csv
from src.etl.pipeline import ETLPipeline
from src.etl.load import ETLLoader
from src.etl.config import ETLConfig

from src.config.settings import Settings

from src.transforms.dimensions import (
    transform_item_dimension,
    transform_store_dimension,
)

item_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_item_dimension,

    source_path=Settings.paths["paths"]["raw_data"]["sales"],

    target_table="item_dim",

    input_required_columns=[
        "item_id",
        "dept_id",
        "cat_id",
    ],

    output_required_columns=[
        "item_id",
        "dept_id",
        "cat_id",
    ],
    output_null_check_columns=[
        "item_id",
        "dept_id",
        "cat_id",
    ],
)

store_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_store_dimension,

    source_path=Settings.paths["paths"]["raw_data"]["sales"],

    target_table="store_dim",

    input_required_columns=[
        "store_id",
        "state_id",
    ],

    output_required_columns=[
        "store_id",
        "state_id",
    ],

    output_null_check_columns=[
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