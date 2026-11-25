
from planner import create_plan, validate_plan

from tools.calculator import calculator
from tools.datetime_tool import get_datetime
from tools.weather import get_weather
from tools.file_tool import create_file, read_file

from memory.history import save_history


# Execute the selected tool
def execute_tool(tool_name, arguments):

    try:

        if not isinstance(arguments, dict):
            return "Error: Invalid tool arguments"

        if tool_name == "calculator":
            return calculator(arguments["expression"])

        elif tool_name == "datetime":
            return get_datetime()

        elif tool_name == "weather":
            return get_weather(arguments["city"])

        elif tool_name == "file":

            action = arguments["action"]

            if action == "create":
                return create_file(
                    arguments["filename"],
                    arguments["content"]
                )

            elif action == "read":
                return read_file(arguments["filename"])

            else:
                return "Error: Invalid file action"

        else:
            return "Error: Unknown tool"

    except Exception as e:
        return f"Error: Tool execution failed: {str(e)}"


# Run the AI agent
def run_agent(user_instruction):

    # Generate task plan
    plan = create_plan(user_instruction)

    # Validate the generated plan again
    plan = validate_plan(plan)

    # Handle planning errors
    if isinstance(plan, dict) and "error" in plan:

        result = {
            "instruction": user_instruction,
            "status": "failed",
            "error": plan["error"],
            "results": []
        }

        save_history(user_instruction, result)

        return result

    results = []

    # Execute each task
    for task in plan:

        tool_name = task["tool"]
        arguments = task["arguments"]

        print(f"\nExecuting: {task['task']}")

        tool_result = execute_tool(tool_name, arguments)

        results.append({
            "task": task["task"],
            "tool": tool_name,
            "result": tool_result
        })

    # Check for tool errors
    has_error = False

    for item in results:

        tool_result = item["result"]

        if isinstance(tool_result, str) and tool_result.startswith("Error"):
            has_error = True

        elif isinstance(tool_result, dict) and "error" in tool_result:
            has_error = True

    # Determine execution status
    if has_error:
        status = "completed_with_errors"
    else:
        status = "completed"

    # Prepare final result
    result = {
        "instruction": user_instruction,
        "status": status,
        "results": results
    }

    # Save conversation history
    save_history(user_instruction, result)

    return result
