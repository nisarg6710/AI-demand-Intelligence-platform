from src.ai.rag.document_loader import DocumentLoader
from src.ai.rag.text_chunker import TextChunker
from src.ai.rag.embedding_generator import EmbeddingGenerator


def main():

    documents = DocumentLoader().load_documents()

    chunks = TextChunker().chunk_documents(
        documents
    )

    embedded_chunks = EmbeddingGenerator().embed_chunks(
        chunks
    )

    print()

    print("Embedding Test")
    print("=" * 60)

    print()

    print(f"Total Chunks : {len(embedded_chunks)}")

    print()

    first = embedded_chunks[0]

    print("Source :", first["source"])
    print("Category :", first["category"])

    print()

    print("Embedding Dimension:")

    print(len(first["embedding"]))

    print()

    print("First 10 Values:")

    print(first["embedding"][:10])


if __name__ == "__main__":
    main()