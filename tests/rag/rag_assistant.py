from src.ai.rag.pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    print()

    print("=" * 70)

    print("Retail Demand Intelligence Assistant")

    print("=" * 70)

    print()

    print("Ask business questions about previous forecasts.")

    print("Type 'exit' to quit.")

    print()

    while True:

        question = input("> ").strip()

        if question.lower() in [

            "exit",

            "quit",

            "q",

        ]:

            print()

            print("Goodbye!")

            break

        if not question:

            continue

        print()

        result = pipeline.ask(question)

        print("Answer")

        print("-" * 70)

        print()

        print(result["answer"])

        print()

        print("Sources")

        print("-" * 70)

        for source in result["sources"]:

            print(

                f"- {source['source']} "

                f"({source['category']})"

            )

        print()

        print("=" * 70)

        print()


if __name__ == "__main__":

    main()