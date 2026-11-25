
from planner import validate_plan

# Test 1: Valid calculator task
valid_plan = [
    {
        "task": "Calculate 100 + 200",
        "tool": "calculator",
        "arguments": {
            "expression": "100 + 200"
        }
    }
]

# Test 2: Invalid tool
invalid_plan = [
    {
        "task": "Send an email",
        "tool": "email",
        "arguments": {}
    }
]

print("TEST 1: Valid Plan")
print(validate_plan(valid_plan))

print("\nTEST 2: Invalid Plan")
print(validate_plan(invalid_plan))
