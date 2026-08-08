from src.ai.tools.sql_tool import SQLTool


def main():

    tool = SQLTool()

    result = tool.execute(
        """
        SELECT *
        FROM calendar_dim
        LIMIT 5;
        """
    )

    print()

    print("=" * 80)

    print("SUCCESS")

    print(result["success"])

    print()

    print("=" * 80)

    print("METADATA")

    print(result["metadata"])

    print()

    print("=" * 80)

    print("DATA")

    print(result["data"])


if __name__ == "__main__":
    main()