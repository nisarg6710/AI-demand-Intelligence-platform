from src.ai.llm.gemini_client import GeminiClient


def main():

    client = GeminiClient()

    response = client.generate(
        system_prompt="You are a helpful AI assistant.",
        user_prompt="Say hello in one sentence."
    )

    print("\nGemini Response")
    print("-" * 40)
    print(response)


if __name__ == "__main__":
    main()