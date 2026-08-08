from src.analytics.service import AnalyticsService

service = AnalyticsService()

df = service.get_monthly_sales()

print(df)