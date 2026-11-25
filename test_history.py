
from memory.history import save_history, get_history

instruction = "Test automatic history saving"

result = {
    "status": "completed",
    "answer": 300
}

print("\nSaving history...")

message = save_history(instruction, result)

print(message)

print("\nChecking saved history...")

history = get_history()

print(history)
