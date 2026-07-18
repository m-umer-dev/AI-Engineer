from ollama import chat

print("=== AI Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input  = input("You: ")

    if user_input.lower() == "exit":
        print("GoodBye")
        break

    response = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
    )

    print("\nAI:", response["message"]["content"])
    print()