import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"


def save_history(instruction, result):

    try:
        os.makedirs("data", exist_ok=True)

        history = []

        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = json.load(file)

        record = {
            "timestamp": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"),
            "instruction": instruction,
            "result": result
        }

        history.append(record)

        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, default=str)

        return "History saved successfully"

    except Exception as e:
        return f"History error: {str(e)}"


def get_history():

    try:
        if not os.path.exists(HISTORY_FILE):
            return []

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []
