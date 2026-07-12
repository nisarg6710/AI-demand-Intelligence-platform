import numpy as np
from pprint import pprint

from src.ai.metadata import ForecastMetadataBuilder


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

    metadata = ForecastMetadataBuilder.build(
        actual,
        forecast,
    )

    print("\nForecast Metadata")
    print("-" * 40)

    pprint(metadata)


if __name__ == "__main__":
    main()