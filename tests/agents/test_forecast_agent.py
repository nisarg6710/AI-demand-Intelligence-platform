from src.ai.agents.forecast_agent import ForecastAgent


agent = ForecastAgent()

# result = agent.run(
#     "Which forecasting model performs best?"
# )
# result = agent.run(
#     "Compare all forecasting models."
# )

# result = agent.run(
#     "Show Prophet predictions."
# )

result = agent.run("Show all forecasting experiments.")

print(result["selected_action"])
print()
print(result["response"])