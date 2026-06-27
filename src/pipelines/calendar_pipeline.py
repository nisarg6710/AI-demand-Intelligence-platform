from src.etl.config import ETLConfig
from src.etl.pipeline import ETLPipeline
from src.etl.load import ETLLoader

from src.etl.extract import extract_csv
from src.transforms.calendar import transform_calendar
from src.config.settings import Settings

calendar_config = ETLConfig(

    extractor=extract_csv,

    transformer=transform_calendar,

    source_path=Settings.paths['paths']['raw_data']['calendar'],

    target_table="calendar_dim",

    required_columns=[
        "date",
        "wm_yr_wk",
        "weekday",
        "wday",
        "month",
        "year",
        "d",
        "event_name_1",
        "event_type_1",
        "event_name_2",
        "event_type_2",
        "snap_CA",
        "snap_TX",
        "snap_WI",
    ],

    # We DO NOT check event columns because NULL is valid there.
    null_check_columns=[
        "date",
        "wm_yr_wk",
        "weekday",
        "d",
    ],
)


def run_calendar_pipeline():

    ETLPipeline.run(
        config=calendar_config,
        loader=ETLLoader,
    )