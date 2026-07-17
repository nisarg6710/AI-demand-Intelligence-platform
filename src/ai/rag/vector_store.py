import faiss
import numpy as np
import pickle
from pathlib import Path


class VectorStore:

    def __init__(self):

        self.index = None
        self.metadata = []

    def build_index(
        self,
        embedded_chunks,
    ):

        embeddings = np.array(
            [
                chunk["embedding"]
                for chunk in embedded_chunks
            ],
            dtype=np.float32,
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings
        )

        self.metadata = embedded_chunks

    def save(
        self,
        index_path="artifacts/faiss/index.faiss",
        metadata_path="artifacts/faiss/metadata.pkl",
    ):

        Path(index_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        faiss.write_index(
            self.index,
            index_path,
        )

        with open(
            metadata_path,
            "wb",
        ) as f:

            pickle.dump(
                self.metadata,
                f,
            )

    def load(
        self,
        index_path="artifacts/faiss/index.faiss",
        metadata_path="artifacts/faiss/metadata.pkl",
    ):

        self.index = faiss.read_index(
            index_path
        )

        with open(
            metadata_path,
            "rb",
        ) as f:

            self.metadata = pickle.load(
                f
            )