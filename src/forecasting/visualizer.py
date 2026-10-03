from pathlib import Path

import matplotlib.pyplot as plt


class ForecastVisualizer:

    @staticmethod
    def plot(
        train,
        test,
        predictions,
        model_name,
    ):

        output_dir = Path("artifacts/forecasts")

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path = (
            output_dir /
            f"{model_name}_forecast.png"
        )

        plt.figure(figsize=(15, 6))

        plt.plot(
            train["date"],
            train["sales"],
            label="Train",
        )

        plt.plot(
            test["date"],
            test["sales"],
            label="Actual",
        )

        plt.plot(
            test["date"],
            predictions,
            label="Prediction",
        )

        plt.legend()

        plt.title(
            f"{model_name} Forecast"
        )

        plt.savefig(
            output_path,
            bbox_inches="tight",
        )

        plt.close()

        return output_path