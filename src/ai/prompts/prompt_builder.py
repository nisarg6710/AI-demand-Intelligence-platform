from src.ai.prompts.templates import SYSTEM_PROMPT


class PromptBuilder:

    @staticmethod
    def build(metadata):

        trend = metadata["trend"]
        seasonality = metadata["seasonality"]
        statistics = metadata["statistics"]

        prompt = f"""
Forecast Metadata

Trend
------
Direction: {trend['direction']}
Growth: {trend['growth_percent']}%

Seasonality
-----------
Weekly Seasonality: {seasonality['weekly_seasonality']}
Strength: {seasonality['seasonality_strength']}

Statistics
----------
Average Demand: {statistics['mean']}
Minimum Demand: {statistics['minimum']}
Maximum Demand: {statistics['maximum']}
Volatility (Std Dev): {statistics['std_dev']}

Explain:

1. Why demand is changing.
2. What the trend indicates.
3. Whether seasonality is important.
4. What inventory strategy should be adopted.
5. Summarize the forecast in plain business language.
"""

        return {

            "system_prompt": SYSTEM_PROMPT,

            "user_prompt": prompt,

        }