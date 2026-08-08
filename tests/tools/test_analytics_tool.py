from src.ai.tools.analytics_tool import AnalyticsTool

tool = AnalyticsTool()

result = tool.get_sales_summary()

print("Success :", result["success"])
print("Metadata:", result["metadata"])
print("Data:")
print(result["data"])
print("Error:")
print(result["error"])