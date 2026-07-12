import yaml

from google import genai

class GeminiClient:

    def __init__(self):

        with open(
            'configs/llm.yaml',
            'r'
        ) as file:
            
            config = yaml.safe_load(file)
        
        self.client = genai.Client(
            api_key = config['api_key']
        )
        self.model = config['model']
    
    def generate(
            self,
            system_prompt,
            user_prompt
    ):
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=f"""
{system_prompt}

{user_prompt}
"""
)

        return response.text