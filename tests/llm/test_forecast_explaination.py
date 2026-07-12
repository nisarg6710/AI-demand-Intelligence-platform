import numpy as np

from src.ai.metadata import ForecastMetadataBuilder
from src.ai.prompts.prompt_builder import PromptBuilder
from src.ai.llm.gemini_client import GeminiClient


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

    prompts = PromptBuilder.build(
        metadata
    )

    client = GeminiClient()

    explanation = client.generate(
        prompts["system_prompt"],
        prompts["user_prompt"],
    )

    print("\nBusiness Explanation")
    print("=" * 70)
    print(explanation)


if __name__ == "__main__":
    main()