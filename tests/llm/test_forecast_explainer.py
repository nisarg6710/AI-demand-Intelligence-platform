import numpy as np

from src.ai.explainer import ForecastExplainer


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
        130,
        132,
        135,
        140,
        145,
        130,
        132,
        135,
        140,
        145,
    ])

    explainer = ForecastExplainer()

    result = explainer.explain(
        actual,
        forecast,
    )

    print("\nForecast Explanation")
    print("=" * 70)

    print(result["explanation"])

    print('\nReport saved at:')
    print(result['report_path'])

    print()

    print("Markdown Report:")
    print(result['report_path'])

    print()

    print("HTML Report:")
    print(result['html_report'])


if __name__ == "__main__":
    main()