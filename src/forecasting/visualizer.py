import matplotlib.pyplot as plt


class ForecastVisualizer:

    @staticmethod
    def plot(train, test, predictions):

        plt.figure(figsize=(15,6))

        plt.plot(
            train["date"],
            train["sales"],
            label="Train"
        )

        plt.plot(
            test["date"],
            test["sales"],
            label="Actual"
        )

        plt.plot(
            test["date"],
            predictions,
            label="Prediction"
        )

        plt.legend()

        plt.title("Forecast")

        plt.show()