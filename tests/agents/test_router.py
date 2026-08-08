from src.ai.agents.router import TaskRouter


def main():

    router = TaskRouter()

    test_cases = [
        (
            "What is the best forecasting model?",
            ["forecast"]
        ),

        (
            "Predict demand for next month.",
            ["forecast"]
        ),

        (
            "Which products are selling the fastest?",
            ["inventory"]
        ),

        (
            "Which products should be prioritized for replenishment?",
            ["inventory"]
        ),

        (
            "Give me an inventory health summary.",
            ["inventory"]
        ),

        (
            "Show me the monthly sales trend.",
            ["analytics"]
        ),

        (
            "Which stores performed the best?",
            ["analytics"]
        ),

        (
            "Show me the SQL query for monthly sales.",
            ["sql"]
        ),

        (
            "Give me an executive report.",
            ["forecast", "analytics", "inventory"]
        ),
    ]

    for question, expected in test_cases:

        result = router.route(question)

        print("\n" + "=" * 80)
        print("Question:", question)
        print("Expected:", expected)
        print("Actual  :", result)

        if result == expected:
            print("PASS")
        else:
            print("FAIL")


if __name__ == "__main__":
    main()