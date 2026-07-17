from src.ai.rag.document_loader import DocumentLoader
from src.ai.rag.text_chunker import TextChunker
from src.ai.rag.embedding_generator import EmbeddingGenerator
from src.ai.rag.vector_store import VectorStore


def main():

    documents = DocumentLoader().load_documents()

    chunks = TextChunker().chunk_documents(
        documents
    )

    embedded = EmbeddingGenerator().embed_chunks(
        chunks
    )

    store = VectorStore()

    store.build_index(
        embedded
    )

    store.save()

    print()

    print("Vector Store Created")
    print("=" * 60)

    print()

    print(
        f"Vectors Stored : {store.index.ntotal}"
    )

    print()

    print(
        "Saved to:"
    )

    print(
        "artifacts/faiss/"
    )


if __name__ == "__main__":
    main()