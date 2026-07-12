import numpy as np

from src.ai.metadata import ForecastMetadataBuilder
from src.ai.prompts.prompt_builder import PromptBuilder


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

    prompt = PromptBuilder.build(
        metadata
    )

    print("\nSystem Prompt")
    print("-" * 40)
    print(prompt["system_prompt"])

    print("\nUser Prompt")
    print("-" * 40)
    print(prompt["user_prompt"])


if __name__ == "__main__":
    main()