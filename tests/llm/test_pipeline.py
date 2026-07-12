import numpy as np

from src.ai.pipeline import ForecastExplanationPipeline


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

    pipeline = ForecastExplanationPipeline()

    result = pipeline.run(
        actual,
        forecast,
    )

    print("\nForecast Explanation")
    print("=" * 70)

    print(result["explanation"])

    print()

    print("Metadata:")
    print(result["metadata_path"])

    print()

    print("Prompt Files:")
    print(result["prompt_paths"])

    print()

    print("Markdown:")
    print(result["report_path"])

    print()

    print("HTML:")
    print(result["html_report"])


if __name__ == "__main__":
    main()