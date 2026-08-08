from src.ai.agents.inventory_agent import InventoryAgent


def main():

    agent = InventoryAgent()

    actions = [
        "get_inventory_summary",
        "get_fast_moving_products",
        "get_slow_moving_products",
        "get_store_inventory",
        "get_reorder_candidates",
        "get_inventory_health",
    ]

    for action in actions:

        print("\n" + "=" * 80)
        print("ACTION:", action)
        print("=" * 80)

        result = agent._execute_action(action)

        print("Success:", result["success"])
        print("Metadata:", result["metadata"])

        print("Result:")
        print(result["data"])

        print("Error:")
        print(result["error"])


if __name__ == "__main__":
    main()