from src.ai.agents.base_agent import BaseAgent
from src.ai.tools.forecast_tool import ForecastTool


class ForecastAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.tool = ForecastTool()

    def _build_prompt(self, question: str):

        return f"""
    User Question:
    {question}

    Available tool actions:

    1. get_best_model
    - Use when the user asks for the best forecasting model.

    2. compare_models
    - Use when the user wants to compare forecasting models.

    3. get_predictions
    - Use when the user asks for future demand predictions.
    - If the user specifies a model, use that model.
    - If the user does NOT specify a model, use best_model.

    4. get_experiments
    - Use when the user asks about forecasting experiments.

    5. get_future_forecast
    - Use when the user asks for future demand forecasts.
    - If the user does not specify a forecast horizon, use 12 months.

    Return ONLY the action name.

    If get_predictions is required, also return the model name.

    Examples:

    Question:
    Which forecasting model performs best?

    Answer:
    get_best_model

    Question:
    Compare forecasting models.

    Answer:
    compare_models

    Question:
    Show Prophet predictions.

    Answer:
    get_predictions ProphetModel

    Question:
    Forecast demand for the next 12 months.

    Answer:
    get_future_forecast 12

    Question:
    Show all forecasting experiments.

    Answer:
    get_experiments

    Return your response in exactly one of the following formats:

    get_best_model
    compare_models
    get_experiments
    get_predictions <ModelName>

    Do not include explanations, punctuation, markdown, or any additional text.
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
You are a senior demand forecasting expert.

Your responsibilities are:

- choose the correct forecasting tool action
- explain demand forecasts
- identify trends
- explain seasonality
- discuss forecast confidence
- answer ONLY forecasting questions

Do not discuss inventory policies.
Do not discuss SQL.
Do not answer unrelated business questions.
"""

    def _execute_action(self, action: str):
        """
        Executes the selected ForecastTool action.

        Handles minor formatting variations returned by the LLM,
        such as:
            get_predictions BestModel
            get_predictions best_model
            get_predictions get_best_model
        """

        try:

            action = action.strip()

            parts = action.split(maxsplit=1)

            if not parts:
                raise ValueError("No forecasting action returned.")

            action_name = parts[0].strip().lower()

            # --------------------------------------------------
            # Best model
            # --------------------------------------------------

            if action_name == "get_best_model":

                return self.tool.get_best_model()

            # --------------------------------------------------
            # Compare models
            # --------------------------------------------------

            elif action_name == "compare_models":

                return self.tool.compare_models()

            # --------------------------------------------------
            # Experiments
            # --------------------------------------------------

            elif action_name == "get_experiments":

                return self.tool.get_experiments()

            elif action_name == "get_future_forecast":

                periods = 12

                if len(parts) >= 2:

                    try:
                        periods = int(parts[1])

                    except ValueError:
                        periods = 12

                return self.tool.get_future_forecast(periods)


            # --------------------------------------------------
            # Predictions
            # --------------------------------------------------



            elif action_name == "get_predictions":

                if len(parts) < 2:

                    raise ValueError(
                        "Model name not provided."
                    )

                model_name = parts[1].strip()


                # --------------------------------------------------
                # Normalize LLM-generated best-model aliases
                # --------------------------------------------------

                normalized_model = (
                    model_name
                    .lower()
                    .replace("-", "_")
                    .replace(" ", "_")
                )

                if normalized_model in {
                    "best_model",
                    "bestmodel",
                    "get_best_model",
                }:

                    model_name = "best_model"

                return self.tool.get_predictions(model_name)

            # --------------------------------------------------
            # Unknown action
            # --------------------------------------------------

            else:

                raise ValueError(
                    f"Unknown forecasting action: {action}"
                )

        except Exception as e:

            return self.tool.failure(str(e))

    def _explain_results(self, question: str, tool_result):
        """
        Uses the LLM to explain forecasting results.
        """

        if not tool_result["success"]:
            return tool_result["error"]

        data = tool_result["data"]

        prompt = f"""
    User Question:
    {question}

    Forecast Data:
    {data.to_string(index=False)}

    Provide a concise business-focused explanation of the
    future demand forecast.

    Your response should include:

    1. Forecast Summary
    - Explain the expected demand over the forecast horizon.

    2. Key Insights
    - Identify high and low forecast periods.
    - Mention notable changes in expected demand.

    3. Trend and Seasonality
    - Explain whether demand appears to increase,
    decrease, or remain stable.
    - Mention relevant seasonal patterns if visible.

    4. Business Implications
    - Explain what the forecast means for inventory,
    staffing, procurement, and operations.

    5. Recommendations
    - Provide practical actions based on the forecast.

    Important:
    - Do not invent numbers.
    - Use only the supplied forecast data.
    - Clearly distinguish predictions from historical observations.
    - Keep the explanation professional and concise.
    """

        return self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=prompt,
        )

    def run(self, question: str):
        """
        Complete ForecastAgent workflow.
        """

        action = self._choose_action(question)

        tool_result = self._execute_action(action)

        explanation = self._explain_results(
            question,
            tool_result,
        )

        return {
            "question": question,
            "selected_action": action,
            "tool_result": tool_result,
            "response": explanation,
        }