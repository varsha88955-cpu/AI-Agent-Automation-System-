
import json
from llm import generate_response


# Validate the AI-generated task plan
def validate_plan(plan):

    if not isinstance(plan, list):
        return {"error": "Task plan must be a list"}

    if not plan:
        return {"error": "Task plan is empty"}

    for task in plan:

        if not isinstance(task, dict):
            return {"error": "Invalid task format"}

        if "task" not in task or "tool" not in task:
            return {"error": "Task description or tool is missing"}

        if not isinstance(task["task"], str) or not task["task"].strip():
            return {"error": "Invalid task description"}

        tool = task["tool"]
        arguments = task.get("arguments", {})

        if not isinstance(arguments, dict):
            return {"error": "Tool arguments must be a dictionary"}

        # Calculator validation
        if tool == "calculator":

            if "expression" not in arguments:
                return {"error": "Calculator expression is missing"}

        # Date and time validation
        elif tool == "datetime":

            pass

        # Weather validation
        elif tool == "weather":

            if "city" not in arguments:
                return {"error": "Weather city is missing"}

        # File validation
        elif tool == "file":

            action = arguments.get("action")

            if action not in ["create", "read"]:
                return {"error": "Invalid file action"}

            if "filename" not in arguments:
                return {"error": "File name is missing"}

            if action == "create" and "content" not in arguments:
                return {"error": "File content is missing"}

        else:

            return {"error": f"Unsupported tool: {tool}"}

    return plan


# Generate a task plan
def create_plan(user_instruction):

    prompt = f"""
    You are an AI task planner.

    Break the user's instruction into smaller tasks.

    Return ONLY a valid JSON list.

    Each task must contain:
    - task: description
    - tool: tool name
    - arguments: required input arguments

    Available tools and arguments:

    1. calculator:
       expression

    2. datetime:
       no arguments

    3. weather:
       city

    4. file:
       action (create or read)
       filename
       content (required for create)

    Example:

    [
        {{
            "task": "Calculate 100 + 200",
            "tool": "calculator",
            "arguments": {{
                "expression": "100 + 200"
            }}
        }},
        {{
            "task": "Get today's date",
            "tool": "datetime",
            "arguments": {{}}
        }}
    ]

    User instruction:
    {user_instruction}
    """

    try:

        response = generate_response(prompt)

        plan = json.loads(response)

        return validate_plan(plan)

    except json.JSONDecodeError:

        return {"error": "Unable to create a valid task plan"}

    except Exception as e:

        return {"error": str(e)}
