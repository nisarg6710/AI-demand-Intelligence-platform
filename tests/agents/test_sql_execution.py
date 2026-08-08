from src.ai.agents.sql_agent import SQLAgent


def main():

    agent = SQLAgent()

    sql = agent._generate_sql(
        "Show the total sales for each store."
    )

    print("=" * 80)
    print("GENERATED SQL")
    print("=" * 80)
    print(sql)

    result = agent._execute_sql(sql)

    print("\n" + "=" * 80)
    print("SUCCESS")
    print("=" * 80)
    print(result["success"])

    print("\n" + "=" * 80)
    print("METADATA")
    print("=" * 80)
    print(result["metadata"])

    print("\n" + "=" * 80)
    print("RESULT")
    print("=" * 80)
    print(result["data"])


if __name__ == "__main__":
    main()