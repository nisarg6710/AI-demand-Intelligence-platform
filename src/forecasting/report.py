import pandas as pd
import os


class ForecastReport:

    @staticmethod
    def generate(results):

        os.makedirs("artifacts", exist_ok=True)

        df = pd.DataFrame([
            {
                "Model": r.model_name,
                "MAE": r.mae,
                "RMSE": r.rmse,
                "MAPE": r.mape,
                "Train Time": r.train_time,
                "Predict Time": r.predict_time
            }
            for r in results
        ])

        df.sort_values("RMSE", inplace=True)

        df.to_csv(
            "artifacts/classical_model_comparison.csv",
            index=False
        )

        df.to_markdown(
            "artifacts/classical_model_comparison.md",
            index=False
        )

        print(df)