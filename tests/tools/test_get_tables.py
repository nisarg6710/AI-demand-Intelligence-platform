from src.ai.tools.sql_tool import SQLTool


def main():

    tool = SQLTool()

    # result = tool.get_tables()

    ##result = tool.get_schema('calendar_dim')

    schema = tool.get_database_schema()

    # print(result)
    ##print(result['data'])

    for table, df in schema['data'].items():
        print()

        print(table)

        print(df)


if __name__ == "__main__":
    main()