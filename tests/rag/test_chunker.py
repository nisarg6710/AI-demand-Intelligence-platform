from src.ai.rag.document_loader import DocumentLoader
from src.ai.rag.text_chunker import TextChunker


def main():

    documents = DocumentLoader().load_documents()

    chunker = TextChunker()

    chunks = chunker.chunk_documents(
        documents
    )

    print()

    print("Chunk Statistics")
    print("=" * 60)

    print()

    print(f"Documents : {len(documents)}")

    print(f"Chunks    : {len(chunks)}")

    print()

    for i, chunk in enumerate(chunks[:5], start=1):

        print(f"Chunk {i}")

        print("-" * 40)

        print("Source :", chunk["source"])

        print("Category :", chunk["category"])

        print()

        print(chunk["text"][:200])

        print()

        print("=" * 60)


if __name__ == "__main__":
    main()