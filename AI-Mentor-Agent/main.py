from agent.agent import AIAgent

agent = AIAgent()

while(True):

    user_input = input("You: ")

    if user_input == "exit":
        break

    response = agent.chat(user_input)

    print("\nAI:", response)