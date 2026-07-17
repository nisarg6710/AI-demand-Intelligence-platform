class TextChunker:

    def __init__(
        self,
        chunk_size=500,
        overlap=100,
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_document(
        self,
        document,
    ):

        text = document["content"]

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(

                {

                    "text": chunk,

                    "source": document["name"],

                    "category": document["category"],

                    "path": document["path"],

                }

            )

            start += self.chunk_size - self.overlap

        return chunks

    def chunk_documents(
        self,
        documents,
    ):

        all_chunks = []

        for document in documents:

            all_chunks.extend(

                self.chunk_document(
                    document
                )

            )

        return all_chunks