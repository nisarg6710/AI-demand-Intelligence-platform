from src.ai.agents.inventory_agent import InventoryAgent


def main():

    agent = InventoryAgent()

    questions = [
        "Give me an inventory summary.",
        "Which products are selling the fastest?",
        "Which products are slow moving?",
        "Which stores need the most inventory support?",
        "Which products should we prioritize for replenishment?",
        "How healthy is our inventory?",
    ]

    for question in questions:

        print("\n" + "=" * 80)
        print(question)
        print("=" * 80)

        action = agent._choose_action(question)

        print("Selected Action:")
        print(action)


if __name__ == "__main__":
    main()