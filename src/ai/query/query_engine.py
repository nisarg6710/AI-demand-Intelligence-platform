from src.ai.agents.orchestrator import AgentOrchestrator


class QueryEngine:
    """
    Public interface for the AI agent system.

    Provides a single entry point for processing
    natural-language business questions.
    """

    def __init__(self):
        self.orchestrator = AgentOrchestrator()

    def ask(self, question: str):
        """
        Process a natural-language business question.

        Returns a structured response containing:
        - success status
        - original question
        - selected agents
        - specialist responses
        - executive report
        """

        # --------------------------------------------------
        # Input validation
        # --------------------------------------------------

        if not isinstance(question, str):

            return {
                "success": False,
                "error": "Question must be a string.",
            }

        question = question.strip()

        if not question:

            return {
                "success": False,
                "error": "Question cannot be empty.",
            }

        # --------------------------------------------------
        # Execute agent workflow
        # --------------------------------------------------

        try:

            result = self.orchestrator.run(question)

            return {
                "success": True,
                "question": question,
                **result,
            }

        except Exception as e:

            return {
                "success": False,
                "question": question,
                "error": str(e),
            }