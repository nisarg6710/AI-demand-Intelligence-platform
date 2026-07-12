from src.ai.explainer import ForecastExplainer


class ForecastExplanationPipeline:

    def __init__(self):

        self.explainer = ForecastExplainer()

    def run(
        self,
        actual,
        forecast,
    ):

        return self.explainer.explain(
            actual,
            forecast,
        )