from src.ai.query.query_engine import QueryEngine


engine = QueryEngine()


questions = {
    "What is the best forecasting model?": ["forecast"],
    "Which products are selling the fastest?": ["inventory"],
    "Show me the monthly sales trend.": ["analytics"],
    "Show me the SQL query for monthly sales.": ["sql"],
    "Give me an executive report.": [
        "forecast",
        "analytics",
        "inventory",
    ],
}


for question, expected_agents in questions.items():

    print("=" * 90)

    print("QUESTION:")
    print(question)

    result = engine.ask(question)

    actual_agents = result.get("selected_agents", [])

    print("\nEXPECTED:")
    print(expected_agents)

    print("ACTUAL:")
    print(actual_agents)

    if actual_agents == expected_agents:
        print("PASS")
    else:
        print("FAIL")

    print()