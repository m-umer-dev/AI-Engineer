from ollama import chat
from config import MODEL_NAME

class AIAgent:

    def __init__(self):
        self.model = MODEL_NAME

    def chat(self,message):
        file_path = "prompts/teacher_prompt.txt"

        with open(file_path, "r", encoding="utf-8") as f:
            system_prompt = f.read()

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role":"user",
                    "content": message
                }
            ]
        )
        return response.message.content