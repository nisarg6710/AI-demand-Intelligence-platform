# from src.etl.extract import extract_calendar
# from src.etl.transform import transform_calendar
# # from src.etl.load import load_calendar

# from src.etl.load import ETLLoader
# from src.etl.extract import extract_csv


# calendar = extract_calendar(
#     "data/raw/m5/calendar.csv"
# )

# sales = extract_csv(
#     'data/raw/m5/sales_train_validation.csv'
# )

# calendar = transform_calendar(calendar)

# # load_calendar(
# #     calendar.head(10)
# # )

# ETLLoader.load_dataframe(
#     calendar.head(10),
#     'calendar_dim'
# )

# print("Successfully loaded 10 rows.")

##----------------------------------------------------------

# from src.etl.extract import extract_calendar
# from src.etl.transform import transform_calendar
# from src.etl.load import ETLLoader
# from src.etl.pipeline import ETLPipeline
# from src.pipelines.calendar_pipeline import run_calendar_pipeline




# ETLPipeline.run_pipeline(
#     extractor=extract_calendar,
#     transformer=transform_calendar,
#     loader=ETLLoader,
#     source_path="data/raw/m5/calendar.csv",
#     target_table="calendar_dim",

#     required_columns=[
#         "date",
#         "wm_yr_wk",
#         "weekday",
#         "wday",
#         "month",
#         "year",
#         "d",
#         "event_name_1",
#         "event_type_1",
#         "event_name_2",
#         "event_type_2",
#         "snap_CA",
#         "snap_TX",
#         "snap_WI",
#     ],

#     null_check_columns=[
#         "date",
#         "wm_yr_wk",
#         "weekday",
#         "d"
#     ]
# )


from src.pipelines.calendar_pipeline import run_calendar_pipeline

if __name__ == "__main__":
    run_calendar_pipeline()