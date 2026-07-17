class ContextBuilder:

    def build(
        self,
        retrieved_chunks,
    ):

        separator = "\n\n" + "-" * 80 + "\n\n"

        sections = []

        for chunk in retrieved_chunks:

            sections.append(
                f"""Source: {chunk["source"]}
Category: {chunk["category"]}

{chunk["text"]}"""
            )

        return separator.join(sections)