from src.ai.agents.analytics_agent import AnalyticsAgent
from src.ai.agents.executive_agent import ExecutiveAgent
from src.ai.agents.forecast_agent import ForecastAgent
from src.ai.agents.inventory_agent import InventoryAgent
from src.ai.agents.router import TaskRouter
from src.ai.agents.sql_agent import SQLAgent


class AgentOrchestrator:

    def __init__(self):

        self.router = TaskRouter()

        self.agents = {
            "forecast": ForecastAgent(),
            "analytics": AnalyticsAgent(),
            "inventory": InventoryAgent(),
            "sql": SQLAgent(),
        }

        self.executive = ExecutiveAgent()

    def _extract_response(self, result):
        """
        Converts specialist-agent results into
        a human-readable response.
        """

        if not isinstance(result, dict):
            return str(result)

        # ForecastAgent
        if result.get("response"):
            return result["response"]

        # SQLAgent query-only request
        if result.get("sql") and not result.get("explanation"):
            return (
                "Generated SQL:\n\n"
                + result["sql"]
            )

        # SQLAgent executed query
        if result.get("explanation"):
            return result["explanation"]

        # Error
        if result.get("error"):
            return f"Agent error: {result['error']}"

        return str(result)

    def run(self, task):

        selected_agents = self.router.route(task)

        responses = {}

        for agent_name in selected_agents:

            agent = self.agents[agent_name]

            raw_result = agent.run(task)

            responses[f"{agent_name.title()} Agent"] = (
                self._extract_response(raw_result)
            )

        # If no specialist was selected
        if not responses:

            return {
                "selected_agents": [],
                "specialists": {},
                "executive_report": None,
            }

        # If only one specialist is required,
        # return its response directly.
        if len(responses) == 1:

            return {
                "selected_agents": selected_agents,
                "specialists": responses,
                "executive_report": None,
            }

        # Multiple specialist agents
        executive_prompt = (
            "The following specialists analyzed the business problem.\n\n"
        )

        for name, response in responses.items():

            executive_prompt += f"""
{name}
----------------
{response}

"""

        executive_prompt += """
Combine these findings into one executive report.

Provide:

1. Executive Summary

2. Key Findings

3. Business Risks

4. Recommendations

5. Next Steps
"""

        final_report = self.executive.run(executive_prompt)

        return {

            "selected_agents": selected_agents,

            "specialists": responses,

            "executive_report": final_report,

        }