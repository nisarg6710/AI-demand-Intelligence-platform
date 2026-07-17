from src.ai.rag.pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    result = pipeline.ask(

        "Have we seen this demand pattern before?"

    )

    print()

    print("Question")
    print("=" * 60)

    print(result["question"])

    print()

    print("Answer")
    print("=" * 60)

    print(result["answer"])

    print()

    print("Sources")
    print("=" * 60)

    for source in result["sources"]:

        print(source)


if __name__ == "__main__":
    main()