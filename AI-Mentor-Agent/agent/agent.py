from ollama import chat
from config import MODEL_NAME
from memory.conversation import Conversation

class AIAgent:

    def __init__(self):
        self.model = MODEL_NAME
        self.conversation = Conversation()

        file_path = "prompts/teacher_prompt.txt"

        with open(file_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def chat(self,user_message):

        self.conversation.add_user_message(user_message)

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            *self.conversation.get_messages()
        ]
        
        response = chat(
            model=self.model,
            messages=messages
        )

        ai_reply = response.message.content

        self.conversation.add_ai_message(ai_reply)

        return ai_reply