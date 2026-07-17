from pprint import pprint

from src.ai.rag.document_loader import DocumentLoader


def main():

    loader = DocumentLoader()

    docs = loader.load_documents()

    print()

    print("Documents Loaded")
    print("=" * 60)

    print()

    print(f"Total Documents: {len(docs)}")

    print()

    for document in docs:

        pprint(document)

        print("-" * 60)


if __name__ == "__main__":
    main()