import re
from typing import List
from agent_src.model import ModelInterface
from agent_src.tools import Tool

class Agent:
    def __init__(
        self,
        tools: List[Tool],
        instructions: str
    ):
        # model used by the agent
        self.model = ModelInterface()

        # tools available to the agent
        self.tools = {tool.name: tool for tool in tools}

        # system instructions for the agent
        self.instructions = instructions

    async def run(
        self,
        user_input: str,
    ) -> str:
        pass # Placeholder for the Agent run function to be implemented in the workshop