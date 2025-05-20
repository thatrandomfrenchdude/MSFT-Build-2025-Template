from datetime import datetime
from typing import Callable

class Tool:
    def __init__(self, name: str, func: Callable[[str], str], description: str):
        pass # Placeholder for the Tool init to be implemented in the workshop

    def run(self, arg: str) -> str:
        pass # Placeholder for the Tool run function to be implemented in the workshop

# Example prompt to us the time tool: "What time is it?"
def time_tool() -> str:
    now = datetime.now()
    return f"The current time is {now.strftime('%I:%M%p').lstrip('0').lower()} on {now.strftime('%d %B %Y')}"

# Define available tools
# Placeholder for the tools to be implemented in the workshop

# Build tool descriptions for the instructions
# Placeholder for the tool descriptions to be implemented in the workshop