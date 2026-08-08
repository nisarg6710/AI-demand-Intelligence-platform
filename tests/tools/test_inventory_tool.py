from src.ai.tools.inventory_tool import InventoryTool


def main():

    tool = InventoryTool()

    tests = [
        ("INVENTORY SUMMARY", tool.get_inventory_summary),
        ("FAST MOVING PRODUCTS", tool.get_fast_moving_products),
        ("SLOW MOVING PRODUCTS", tool.get_slow_moving_products),
        ("STORE INVENTORY", tool.get_store_inventory),
        ("REORDER CANDIDATES", tool.get_reorder_candidates),
        ("INVENTORY HEALTH", tool.get_inventory_health),
    ]

    for name, method in tests:

        print("\n" + "=" * 80)
        print(name)
        print("=" * 80)

        result = method()

        print("Success :", result["success"])
        print("Metadata:", result["metadata"])
        print("Data:")
        print(result["data"])
        print("Error:")
        print(result["error"])


if __name__ == "__main__":
    main()