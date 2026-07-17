from src.ai.rag.retriever import Retriever
from src.ai.rag.context_builder import ContextBuilder


def main():

    retriever = Retriever()

    chunks = retriever.retrieve(
        "How should inventory be managed for products with increasing demand?"
    )

    context = ContextBuilder().build(
        chunks
    )

    print()

    print("Generated Context")
    print("=" * 60)

    print()

    print(context)


if __name__ == "__main__":
    main()