from src.analytics.service import AnalyticsService

service = AnalyticsService()

# df = service.get_sales_summary()

# print(type(df))
# print(df)

query = """
SELECT
    COUNT(*) AS total_records,
    SUM(sales) AS total_sales
FROM sales_fact;
"""

df = service._run_query(query)

print(type(df))
print(df)