from src.analytics.service import AnalyticsService

service = AnalyticsService()

# result = service.get_sales_summary()
df = service.get_top_stores()

# print(result["success"])
# print(result["metadata"])
# print(result["data"])

print(df.head())