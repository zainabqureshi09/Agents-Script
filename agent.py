import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.history = []

    def think(self, message):
        self.history.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are an AI Agent named {self.name}. Your job: {self.role}."},
                *self.history
            ]
        )

        answer = response.choices[0].message['content']
        self.history.append({"role": "assistant", "content": answer})
        return answer
