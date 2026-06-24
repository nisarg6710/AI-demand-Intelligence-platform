from src.etl.extract import extract_calendar
from src.etl.transform import transform_calendar
from src.etl.load import load_calendar


calendar = extract_calendar(
    "data/raw/m5/calendar.csv"
)

calendar = transform_calendar(calendar)

load_calendar(
    calendar.head(10)
)

print("Successfully loaded 10 rows.")