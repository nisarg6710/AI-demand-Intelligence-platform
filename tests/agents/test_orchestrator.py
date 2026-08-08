from src.ai.agents.orchestrator import AgentOrchestrator


orchestrator = AgentOrchestrator()

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

    result = orchestrator.run(question)

    print("\nSELECTED AGENTS:")
    print(result["selected_agents"])

    print("\nSPECIALIST RESULTS:")

    for name, response in result["specialists"].items():

        print(f"\n{name}")
        print("-" * 80)
        print(response)

    print("\nEXECUTIVE REPORT:")
    print(result["executive_report"])

    print()