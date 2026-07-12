import numpy as np

from src.ai.analyzers.trend import TrendAnalyzer


def main():

    actual = np.array([

        100,
        105,
        110,
        120,
        125,

    ])

    forecast = np.array([

        130,
        132,
        135,
        140,
        145,

    ])

    result = TrendAnalyzer.analyze(
        actual,
        forecast,
    )

    print("\nTrend Analysis")
    print("-" * 30)

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()