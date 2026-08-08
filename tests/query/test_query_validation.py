from src.ai.query.query_engine import QueryEngine


engine = QueryEngine()


test_cases = [
    None,
    123,
    "",
    "   ",
]


for question in test_cases:

    print("=" * 80)

    print("INPUT:")
    print(repr(question))

    result = engine.ask(question)

    print("\nSUCCESS:")
    print(result["success"])

    print("\nRESULT:")
    print(result)