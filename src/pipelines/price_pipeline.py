from src.etl.config import ETLConfig
from src.etl.extract import extract_csv
from src.transforms.prices import transform_prices
from src.etl.pipeline import ETLPipeline
from src.etl.load import ETLLoader

from src.config.settings import Settings

price_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_prices,

    source_path=Settings.paths["paths"]["raw_data"]["prices"],

    target_table="price_fact",

    required_columns=[
        "store_id",
        "item_id",
        "wm_yr_wk",
        "sell_price",
    ],

    null_check_columns=[
        "store_id",
        "item_id",
        "wm_yr_wk",
        "sell_price",
    ],

    chunksize=50000,
)

def run_price_pipeline():

    ETLPipeline.run(
        price_config,
        ETLLoader
    )