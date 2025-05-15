import requests
import sys
import threading
import time
import yaml

def loading_indicator() -> None:
    """Display a loading indicator in the console while the chat request is being processed"""
    while not stop_loading:
        for _ in range(10):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * 10 + '\r')
        sys.stdout.flush()
    print('')

class Chatbot:
    def __init__(self):
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)

        self.api_key = config["ANYTHING_LLM_API_KEY"]
        self.base_url = config["ANYTHING_LLM_BASE_URL"]
        self.workspace_slug = config["ANYTHING_LLM_WORKSPACE_SLUG"]

        self.chat_url = f"{self.base_url}/workspace/{self.workspace_slug}/chat"

        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.api_key
        }

    def run(self) -> None:
        pass # Placeholder for the chat loop to be implemented in the workshop

    def blocking_chat(self, message: str) -> str:
        """
        Send a chat request to the model server and return the response.
        This function blocks until the response is received.
        
        Inputs:
        - message: The message to send to the chatbot
        """
        global stop_loading
        stop_loading = False
        loading_thread = threading.Thread(target=loading_indicator)
        loading_thread.start()

        data = {
            "message": message,
            "mode": "chat",
            "sessionId": "example-session-id",
            "attachments": []
        }

        chat_response = requests.post(
            self.chat_url,
            headers=self.headers,
            json=data
        )

        stop_loading = True
        loading_thread.join()

        try:
            print("Agent: ", end="")
            print(chat_response.json()['textResponse'])
            print("")
        except ValueError:
            return "Response is not valid JSON"
        except Exception as e:
            return f"Chat request failed. Error: {e}"

if __name__ == '__main__':
    stop_loading = False
    chatbot = Chatbot()
    chatbot.run()