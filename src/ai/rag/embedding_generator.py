from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2",
    ):

        self.model = SentenceTransformer(
            model_name
        )

    def embed_text(
        self,
        text,
    ):

        return self.model.encode(
            text,
            convert_to_numpy=True,
        )

    def embed_chunks(
        self,
        chunks,
    ):

        embeddings = []

        for chunk in chunks:

            vector = self.embed_text(
                chunk["text"]
            )

            chunk["embedding"] = vector

            embeddings.append(chunk)

        return embeddings