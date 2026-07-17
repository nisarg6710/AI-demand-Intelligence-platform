from src.ai.rag.retriever import Retriever
from src.ai.rag.context_builder import ContextBuilder
from src.ai.prompts.rag_prompt_builder import RAGPromptBuilder


def main():

    question = "Have we seen this demand pattern before?"

    chunks = Retriever().retrieve(question)

    context = ContextBuilder().build(chunks)

    builder = RAGPromptBuilder()

    print()

    print("SYSTEM PROMPT")
    print("=" * 60)

    print(builder.system_prompt())

    print()

    print("USER PROMPT")
    print("=" * 60)

    print()

    print(

        builder.user_prompt(
            question,
            context,
        )

    )


if __name__ == "__main__":
    main()