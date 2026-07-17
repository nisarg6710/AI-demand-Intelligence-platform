from src.ai.rag.retriever import Retriever
from src.ai.rag.context_builder import ContextBuilder
from src.ai.prompts.rag_prompt_builder import RAGPromptBuilder
from src.ai.llm.gemini_client import GeminiClient


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

        self.context_builder = ContextBuilder()

        self.prompt_builder = RAGPromptBuilder()

        self.llm = GeminiClient()

    def ask(
        self,
        question,
        top_k=3,
    ):

        retrieved_chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        context = self.context_builder.build(
            retrieved_chunks
        )

        system_prompt = (
            self.prompt_builder.system_prompt()
        )

        user_prompt = (
            self.prompt_builder.user_prompt(
                question,
                context,
            )
        )

        answer = self.llm.generate(

            system_prompt=system_prompt,

            user_prompt=user_prompt,

        )

        unique_sources = []

        seen = set()

        for chunk in retrieved_chunks:

            key = (
                chunk["source"],
                chunk["category"],
            )

            if key not in seen:

                seen.add(key)

                unique_sources.append(

                    {

                        "source": chunk["source"],

                        "category": chunk["category"],

                    }

                )

        return {

            "question": question,

            "answer": answer,

            "context": context,

            "sources": unique_sources,

        }