# from src.ai.agents.sql_agent import SQLAgent


# def main():

# #     agent = SQLAgent()

# #     task = """
# # Write a SQL query to calculate total sales for each store during the last 30 days.
# # """

# #     response = agent.run(task)

# #     print()

# #     print("SQL Agent")

# #     print("=" * 60)

# #     print()

# #     print(response)
## type-2:-
#     agent = SQLAgent()

#     response = agent.run(
#         "Show the total sales for each store."
#     )

#     print(response["sql"])
#     print(response["result"]["data"])
#     print(response["explanation"])



# if __name__ == "__main__":

#     main()

from src.ai.agents.sql_agent import SQLAgent


agent = SQLAgent()

question = "Show me the SQL query for monthly sales."

print("=" * 80)
print("DIRECT SQL AGENT TEST")
print("=" * 80)

result = agent.run(question)

print("TYPE:")
print(type(result))

print("\nRAW RESULT:")
print(result)

print("\nIS NONE:")
print(result is None)

if isinstance(result, dict):
    print("\nKEYS:")
    print(result.keys())

    print("\nSQL:")
    print(result.get("sql"))

    print("\nEXPLANATION:")
    print(result.get("explanation"))

    print("\nRESULT:")
    print(result.get("result"))