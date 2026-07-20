from ollama import chat
from tools import calculator

messages = []

print("=== AI Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input  = input("You: ")

    if user_input.lower() == "exit":
        print("GoodBye")
        break

    messages.append({
        "role": "user",
        "content": user_input,
    })

    response = chat(
        model="qwen2.5:3b",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": ai_reply,
    })

    print("\nAI:", ai_reply)
    print()