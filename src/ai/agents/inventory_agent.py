from src.ai.agents.base_agent import BaseAgent
from src.ai.tools.inventory_tool import InventoryTool


class InventoryAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.tool = InventoryTool()

    def _build_prompt(self, question: str):

        return f"""
User Question:
{question}

Available inventory tool actions:

1. get_inventory_summary
- Use when the user asks for an overall inventory or demand health summary.

2. get_fast_moving_products
- Use when the user asks which products are selling fastest
  or have the highest demand velocity.

3. get_slow_moving_products
- Use when the user asks which products are selling slowly
  or have low demand velocity.

4. get_store_inventory
- Use when the user asks which stores have the highest
  or lowest inventory demand.

5. get_reorder_candidates
- Use when the user asks which products should receive
  replenishment priority.

6. get_inventory_health
- Use when the user asks about overall inventory health,
  product velocity distribution, or inventory risk.

Return ONLY the action name.

Examples:

Question:
Give me an inventory summary.

Answer:
get_inventory_summary

Question:
Which products are selling the fastest?

Answer:
get_fast_moving_products

Question:
Which products are slow moving?

Answer:
get_slow_moving_products

Question:
Which stores need the most inventory support?

Answer:
get_store_inventory

Question:
Which products should we prioritize for replenishment?

Answer:
get_reorder_candidates

Question:
How healthy is our inventory?

Answer:
get_inventory_health

Return your response in exactly one of the following formats:

get_inventory_summary
get_fast_moving_products
get_slow_moving_products
get_store_inventory
get_reorder_candidates
get_inventory_health

Do not include explanations, punctuation, markdown,
or any additional text.
"""

    def _choose_action(self, question: str):

        prompt = self._build_prompt(question)

        response = self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
        )

        return response.strip()

    def system_prompt(self):

        return """
You are a senior inventory and demand planning expert.

Your responsibilities are:

- choose the correct inventory tool action
- analyze product demand velocity
- identify fast-moving products
- identify slow-moving products
- identify replenishment priorities
- analyze store-level demand
- assess inventory health based on historical demand

Important limitation:

The current system does NOT contain:

- current stock quantities
- warehouse inventory levels
- reorder points
- safety stock quantities
- supplier lead times

Therefore, do NOT claim that a product is currently out of stock
or provide a specific reorder quantity.

Use terms such as:

- demand velocity
- replenishment priority
- inventory demand
- fast-moving
- slow-moving
- historical demand

Answer ONLY inventory and demand-planning questions.

Do not discuss SQL.

Do not discuss forecasting models.

Do not answer unrelated business questions.
"""

    def _execute_action(self, action: str):

        if action == "get_inventory_summary":

            return self.tool.get_inventory_summary()

        elif action == "get_fast_moving_products":

            return self.tool.get_fast_moving_products()

        elif action == "get_slow_moving_products":

            return self.tool.get_slow_moving_products()

        elif action == "get_store_inventory":

            return self.tool.get_store_inventory()

        elif action == "get_reorder_candidates":

            return self.tool.get_reorder_candidates()

        elif action == "get_inventory_health":

            return self.tool.get_inventory_health()

        else:

            return self.tool.failure(
                f"Unknown inventory action: {action}"
            )

    def run(self, question: str):

        action = self._choose_action(question)

        result = self._execute_action(action)

        if not result["success"]:
            return f"Inventory analysis failed: {result['error']}"

        data = result["data"]

        explanation_prompt = f"""
    User Question:
    {question}

    Inventory Analysis Action:
    {action}

    Inventory Data:
    {data.to_string(index=False)}

    Provide a clear business-oriented answer to the user's question.

    Important limitations:

    - The system contains historical sales demand data.
    - Inventory quantities are NOT available.
    - Do not claim that a product is currently out of stock.
    - Do not provide exact reorder quantities.
    - Do not invent safety stock or reorder point values.
    - Base conclusions on demand velocity and historical sales.

    Structure the response as:

    1. Executive Summary

    2. Key Findings

    3. Inventory Implications

    4. Recommendations

    Keep the answer concise but useful for a business stakeholder.
    """

        response = self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=explanation_prompt,
        )

        return response.strip()