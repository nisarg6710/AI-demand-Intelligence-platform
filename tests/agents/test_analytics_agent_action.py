from src.ai.agents.analytics_agent import AnalyticsAgent


def main():

    agent = AnalyticsAgent()

    questions = [

        "Give me an overall sales summary.",

        "Which stores performed the best?",

        "Show the top selling products.",

        "Show monthly sales trend.",

        "Analyze weekday sales.",

        "Compare store performance.",

        "Give me pricing statistics.",

        "Show sales distribution.",

        "Which product categories perform best?",

        "Show department performance."

    ]

    for question in questions:

        print("=" * 80)

        print("QUESTION")
        print(question)

        print()

        action = agent._choose_action(question)

        print("ACTION")
        print(action)

        print()
        

if __name__ == "__main__":
    main()