
import ast
import operator


# Allowed mathematical operations
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg
}


def calculate_node(node):

    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return node.value

        raise ValueError("Invalid number")

    elif isinstance(node, ast.BinOp):

        operation = type(node.op)

        if operation not in operators:
            raise ValueError("Unsupported operation")

        left = calculate_node(node.left)
        right = calculate_node(node.right)

        if operation == ast.Pow and abs(right) > 100:
            raise ValueError("Exponent is too large")

        result = operators[operation](left, right)

        if isinstance(result, (int, float)) and abs(result) > 10**100:
            raise ValueError("Result is too large")

        return result

    elif isinstance(node, ast.UnaryOp):

        operation = type(node.op)

        if operation not in operators:
            raise ValueError("Unsupported operation")

        return operators[operation](calculate_node(node.operand))

    else:

        raise ValueError("Invalid mathematical expression")


def calculator(expression):

    try:

        tree = ast.parse(expression, mode="eval")

        return calculate_node(tree.body)

    except ZeroDivisionError:

        return "Error: Cannot divide by zero"

    except (ValueError, SyntaxError, TypeError, OverflowError):

        return "Error: Invalid calculation"

    except Exception:

        return "Error: Calculation failed"
