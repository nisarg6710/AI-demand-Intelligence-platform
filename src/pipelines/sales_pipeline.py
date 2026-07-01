from src.config.settings import Settings

from src.etl.config import ETLConfig
from src.etl.extract import extract_csv
from src.etl.load import ETLLoader
from src.etl.pipeline import ETLPipeline

from src.transforms.sales import transform_sales


sales_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_sales,

    source_path=Settings.paths["paths"]["raw_data"]["sales"],

    target_table="sales_fact",

    # Columns expected in the raw CSV
    input_required_columns=[
        "item_id",
        "store_id",
    ],

    # Columns after transform_sales()
    output_required_columns=[
        "item_id",
        "store_id",
        "d",
        "sales",
    ],

    output_null_check_columns=[
        "item_id",
        "store_id",
        "d",
        "sales",
    ],

    chunksize=100
)


def run_sales_pipeline():

    ETLPipeline.run(
        sales_config,
        ETLLoader
    )