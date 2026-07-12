import numpy as np

from src.ai.analyzers.seasonality import SeasonalityAnalyzer


def main():

    forecast = np.array([

        100,
        105,
        110,
        108,
        106,
        104,
        102,

        100,
        105,
        110,
        108,
        106,
        104,
        102,

    ])

    result = SeasonalityAnalyzer.analyze(
        forecast
    )

    print("\nSeasonality Analysis")
    print("-" * 30)

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()