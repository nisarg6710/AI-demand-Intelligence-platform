import numpy as np

from src.ai.analyzers.statistics import StatisticsAnalyzer


def main():

    forecast = np.array([

        100,
        105,
        110,
        120,
        125,
        130,
        128,
        135,
        140,
        145,

    ])

    result = StatisticsAnalyzer.analyze(
        forecast
    )

    print("\nForecast Statistics")
    print("-" * 30)

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()