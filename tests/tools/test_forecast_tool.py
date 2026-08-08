from src.ai.tools.forecast_tool import ForecastTool


def main():

    tool = ForecastTool()

    result = tool.get_experiments()

    print(result["success"])
    print(result["metadata"])
    print(result["data"].head())


if __name__ == "__main__":
    main()