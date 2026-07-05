import pandas as pd


class ForecastRegistry:

    def __init__(self):

        self.results = []

    def add(self, result):

        self.results.append(result)
    
    def get_results(self):
        return self.results

    def summary(self):

        print("\n========== MODEL COMPARISON ==========\n")

        print(
            f"{'Model':<22}"
            f"{'MAE':>10}"
            f"{'RMSE':>10}"
            f"{'MAPE':>10}"
            f"{'Train(s)':>12}"
            f"{'Predict(s)':>14}"
        )

        data = []

        for r in self.results:

            print(
                f"{r.model_name:<22}"
                f"{r.mae:>10.2f}"
                f"{r.rmse:>10.2f}"
                f"{r.mape:>10.2f}"
                f"{r.train_time:>12.4f}"
                f"{r.predict_time:>14.4f}"
            )