import yaml
from typing import List, Dict, Any
from openai import OpenAI

# A message is a dictionary with a role and content
Message = Dict[str, str]

class ModelInterface:
    def __init__(self):
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
        
        self.model = config.get("MODEL")

        LM_STUDIO_URL = config.get("LM_STUDIO_URL")
        LM_STUDIO_API_KEY = config.get("LM_STUDIO_API_KEY")
        self.client = OpenAI(base_url=LM_STUDIO_URL, api_key=LM_STUDIO_API_KEY)

    def chat_completion(
        self,
        messages: List[Message],
        temperature: float = 0.7
    ) -> Any:
        """Send messages to the language model and get a response."""
        resp = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=temperature
        )
        return resp.choices[0].message.content