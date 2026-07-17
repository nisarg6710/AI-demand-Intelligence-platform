import numpy as np

from src.ai.rag.embedding_generator import EmbeddingGenerator
from src.ai.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingGenerator()

        self.store = VectorStore()

        self.store.load()

    def retrieve(
        self,
        query,
        top_k=3,
    ):

        query_embedding = self.embedder.embed_text(
            query
        )

        query_embedding = np.array(
            [query_embedding],
            dtype=np.float32,
        )

        distances, indices = self.store.index.search(
            query_embedding,
            top_k,
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0],
        ):

            chunk = self.store.metadata[index].copy()

            chunk["distance"] = float(distance)

            results.append(chunk)

        return results