class RAGPromptBuilder:

    def system_prompt(self):

        return """
You are an expert retail demand forecasting consultant.

Answer ONLY using the retrieved business knowledge.

If the retrieved context does not contain the answer,
say that the available knowledge does not provide
enough information.

Never invent business policies.

Always reference the retrieved documents when possible.
"""

    def user_prompt(
        self,
        question,
        context,
    ):

        return f"""
Retrieved Knowledge
===================

{context}

===================

Question:

{question}

Provide a clear business answer based ONLY on the retrieved knowledge.
"""