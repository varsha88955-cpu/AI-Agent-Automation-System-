
from agent import run_agent
from memory.history import get_history
import json

print("================================")
print("       AI AGENT ASSISTANT")
print("================================")

while True:

    instruction = input("\nEnter your instruction (or type exit): ")

    if instruction.lower() == "exit":
        print("Thank you for using AI Agent!")
        break

    elif instruction.lower() == "history":

        history = get_history()

        print("\n========== CONVERSATION HISTORY ==========")

        if not history:
            print("No previous conversations found.")

        else:
            for item in history:
                print("\nTime:", item["timestamp"])
                print("Instruction:", item["instruction"])
                print("Result:")
                print(json.dumps(item["result"], indent=4))

        continue

    result = run_agent(instruction)

    print("\n========== AGENT RESULTS ==========")

    print(json.dumps(result, indent=4, default=str))
