

import os

OUTPUT_FOLDER = "data/generated_files"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def create_file(filename, content):

    try:

        if not isinstance(filename, str) or not filename.strip():
            return "Error: Invalid filename"

        if not isinstance(content, str):
            return "Error: File content must be text"

        filename = filename.strip()

        if not filename.endswith(".txt"):
            filename += ".txt"

        if os.path.basename(filename) != filename:
            return "Error: Invalid filename"

        file_path = os.path.join(OUTPUT_FOLDER, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        return f"File created successfully: {file_path}"

    except OSError as e:

        return f"Error creating file: {str(e)}"


def read_file(filename):

    try:

        if not isinstance(filename, str) or not filename.strip():
            return "Error: Invalid filename"

        filename = filename.strip()

        if not filename.endswith(".txt"):
            filename += ".txt"

        if os.path.basename(filename) != filename:
            return "Error: Invalid filename"

        file_path = os.path.join(OUTPUT_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except FileNotFoundError:

        return "Error: File not found"

    except OSError as e:

        return f"Error reading file: {str(e)}"
