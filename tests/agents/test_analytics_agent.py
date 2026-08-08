from src.ai.agents.analytics_agent import AnalyticsAgent


def main():

    agent = AnalyticsAgent()

    questions = [

        "Give me an overall sales summary.",

        "Which stores performed the best?",

        "Show the top selling products.",

        "Show monthly sales trend.",

        "Analyze weekday sales."

    ]

    for question in questions:

        print("=" * 80)
        print(question)
        print()

        response = agent.run(question)

        print(response)
        print()


if __name__ == "__main__":
    main()