from src.ai.agents.sql_agent import SQLAgent


def main():

    agent = SQLAgent()

    sql = agent._generate_sql(

        "Show the total sales for each store."

    )

    print("=" * 80)
    print(sql)


if __name__ == "__main__":
    main()