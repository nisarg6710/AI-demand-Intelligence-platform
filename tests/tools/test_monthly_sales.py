from src.ai.tools.analytics_tool import AnalyticsTool

tool = AnalyticsTool()

result = tool.get_monthly_sales()

print(result["success"])
print(result["metadata"])
print(result["data"])