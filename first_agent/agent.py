# from ollama import chat
# from tools import calculator

# messages = []

# print("=== AI Agent ===")
# print("Type 'exit' to quit.\n")

# while True:
#     user_input  = input("You: ")

#     if user_input.lower() == "exit":
#         print("GoodBye")
#         break

#     messages.append({
#         "role": "user",
#         "content": user_input,
#     })

#     response = chat(
#         model="qwen2.5:3b",
#         messages=messages
#     )

#     ai_reply = response["message"]["content"]

#     messages.append({
#         "role": "assistant",
#         "content": ai_reply,
#     })

#     print("\nAI:", ai_reply)
#     print()

from tools import calculator

user_input = input("Enter Calculations: ")
part = user_input.split()
num1 = int(part[0])
num2 = int(part[2])
operation = part[1]

result = calculator(num1, num2, operation)

print("Result:", result)

