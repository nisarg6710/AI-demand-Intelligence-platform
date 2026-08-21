from src.ai.agents.base_agent import BaseAgent
from src.ai.tools.analytics_tool import AnalyticsTool


class AnalyticsAgent(BaseAgent):

    def __init__(self):
        super().__init__()

        self.tool = AnalyticsTool()

    def system_prompt(self):

        return """
You are a senior business analytics expert.

Your responsibilities are:

- choose the correct analytics tool action
- analyze retail sales
- explain business KPIs
- identify trends
- compare stores
- compare products
- explain seasonality
- answer ONLY analytics questions

Do not generate SQL.

Do not discuss forecasting models.

Do not recommend inventory policies.
"""

    def _build_prompt(self, question: str):

        return f"""
    User Question:
    {question}

    Available tool actions:

    1. get_sales_summary
    - Overall sales KPIs

    2. get_top_stores
    - Highest selling stores

    3. get_top_products
    - Highest selling products

    4. get_monthly_sales
    - Monthly sales trend

    5. get_weekday_sales
    - Weekday sales trend

    6. get_store_performance
    - Store performance metrics

    7. get_price_summary
    - Price statistics

    8. get_sales_distribution
    - Sales statistics

    9. get_category_performance
    - Category performance

    10. get_department_performance
    - Department performance

    Return ONLY ONE action name.

    Examples

    Question:
    Show monthly sales.

    Answer:
    get_monthly_sales

    Question:
    Top performing stores.

    Answer:
    get_top_stores

    Question:
    Sales summary.

    Answer:
    get_sales_summary

    Question:
    Price analysis.

    Answer:
    get_price_summary

    Return ONLY the action.
    No explanation.
    """

    def _choose_action(self, question: str):
        prompt = self._build_prompt(question)

        response = self.llm.generate(
            system_prompt = self.system_prompt(),
            user_prompt = prompt
        )

        return response.strip()

    def _execute_action(self, action: str):

        action = action.strip()

        if action == "get_sales_summary":
            return self.tool.get_sales_summary()

        elif action == "get_top_stores":
            return self.tool.get_top_stores()

        elif action == "get_top_products":
            return self.tool.get_top_products()

        elif action == "get_monthly_sales":
            return self.tool.get_monthly_sales()

        elif action == "get_weekday_sales":
            return self.tool.get_weekday_sales()

        elif action == "get_store_performance":
            return self.tool.get_store_performance()

        elif action == "get_price_summary":
            return self.tool.get_price_summary()

        elif action == "get_sales_distribution":
            return self.tool.get_sales_distribution()

        elif action == "get_category_performance":
            return self.tool.get_category_performance()

        elif action == "get_department_performance":
            return self.tool.get_department_performance()

        return self.tool.failure(f"Unknown action: {action}")

    def _explain_results(self, question: str, result):

        prompt = f"""
    User Question:
    {question}

    Analytics Result:

    {result['data']}

    Please provide:

    1. Executive Summary
    2. Key Insights
    3. Important Trends
    4. Business Recommendations

    Important data interpretation rules:

    - Treat total_records as sales records, not customer transactions.
    - Treat total_sales as units sold unless the data explicitly represents monetary revenue.
    - Do not call total_sales "revenue".
    - Do not call average_sales "average transaction value".
    - Do not infer customer behavior, customer frequency, or customer demographics unless the provided data supports it.
    - Do not invent business context that is not supported by the analytics result.
    - Clearly distinguish facts from reasonable business interpretations.
    - When discussing zero sales, describe them as zero-unit sales records rather than assuming they are POS errors.
    - Keep the response concise and business-oriented.
    """

        return self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
        )

    def run(self, question: str):

        print("\n========== ANALYTICS AGENT ==========")
        print("Question:", question)

        print("STEP 1: Choosing action...")
        action = self._choose_action(question)

        print("STEP 1 COMPLETE")
        print("Selected action:", action)

        print("STEP 2: Executing tool...")
        tool_result = self._execute_action(action)

        print("STEP 2 COMPLETE")
        print("Tool success:", tool_result.get("success"))

        if not tool_result["success"]:
            print("Tool error:", tool_result.get("error"))
            return tool_result["error"]

        print("STEP 3: Explaining results...")

        result = self._explain_results(
            question,
            tool_result
        )

        print("STEP 3 COMPLETE")
        print("========== ANALYTICS COMPLETE ==========\n")

        return result