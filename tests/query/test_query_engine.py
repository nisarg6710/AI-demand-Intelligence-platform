from src.ai.query.query_engine import QueryEngine


engine = QueryEngine()


questions = [
    "What is the best forecasting model?",
    "Which products are selling the fastest?",
    "Show me the monthly sales trend.",
    "Show me the SQL query for monthly sales.",
    "Give me an executive report.",
]


for question in questions:

    print("=" * 100)

    print("QUESTION:")
    print(question)

    result = engine.ask(question)

    print("\nSUCCESS:")
    print(result["success"])

    if not result["success"]:

        print("\nERROR:")
        print(result["error"])

        continue

    print("\nSELECTED AGENTS:")
    print(result.get("selected_agents"))

    print("\nFINAL RESPONSE:")

    executive_report = result.get("executive_report")

    if executive_report:

        print(executive_report)

    else:

        specialists = result.get("specialists", {})

        for name, response in specialists.items():

            print(f"\n{name}")
            print("-" * 80)

            if isinstance(response, dict):

                if "response" in response:
                    print(response["response"])

                elif "explanation" in response:
                    print(response["explanation"])

                elif "sql" in response:
                    print(response["sql"])

                else:
                    print(response)

            else:
                print(response)

    print()