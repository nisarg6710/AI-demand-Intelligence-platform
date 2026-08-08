from src.ai.agents.sql_agent import SQLAgent


def main():

    agent = SQLAgent()

    sql = agent._generate_sql(
        "Show the total sales for each store."
    )

    result = agent._execute_sql(sql)

    explanation = agent._explain_results(
        "Show the total sales for each store.",
        result,
    )

    print("=" * 80)
    print(explanation)


if __name__ == "__main__":
    main()