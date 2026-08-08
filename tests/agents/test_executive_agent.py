from src.ai.agents.executive_agent import ExecutiveAgent


def main():

    agent = ExecutiveAgent()

    task = """
Business Summary

• Forecasted demand will increase by 15%.

• Weekend sales are 25% higher.

• Store A outperforms Store B by 18%.

• Current inventory covers 3.8 weeks.

Prepare an executive report for senior management.
"""

    response = agent.run(task)

    print()

    print("Executive Agent")

    print("=" * 60)

    print()

    print(response)


if __name__ == "__main__":

    main()