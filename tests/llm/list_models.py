# import yaml
# from google import genai


# with open("configs/llm.yaml", "r") as f:
#     config = yaml.safe_load(f)

# client = genai.Client(api_key=config["api_key"])

# print("\nAvailable Models")
# print("=" * 60)

# for model in client.models.list():
#     print(model.name)

from google import genai
import yaml

with open("configs/llm.yaml") as f:
    config = yaml.safe_load(f)

client = genai.Client(api_key=config["api_key"])

response = client.models.generate_content(
    model="models/gemini-3.5-flash",
    contents="Say hello."
)

print(response.text)