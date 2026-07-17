from src.ai.rag.retriever import Retriever


def main():

    retriever = Retriever()

    query = "How should inventory be managed for products with increasing demand?"

    results = retriever.retrieve(
        query,
        top_k=3,
    )

    print()

    print("Retriever Results")
    print("=" * 60)

    print()

    for i, result in enumerate(results, start=1):

        print(f"Result {i}")

        print("-" * 40)

        print("Source    :", result["source"])

        print("Category  :", result["category"])

        print("Distance  :", round(result["distance"], 4))

        print()

        print(result["text"][:300])

        print()

        print("=" * 60)


if __name__ == "__main__":
    main()