from abc import ABC
from abc import abstractmethod

from src.ai.llm.gemini_client import GeminiClient

class BaseAgent(ABC):

    def __init__(self):

        self.llm = GeminiClient()
    


    @abstractmethod
    def system_prompt(self):

        pass

    def run(self,
            task
    ):
        return self.llm.generate(
            system_prompt=self.system_prompt(),
            user_prompt=task
        )