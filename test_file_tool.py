
from tools.file_tool import create_file, read_file

print("TEST 1: Create file")

print(create_file(
    "sample",
    "This is my AI Agent Automation System."
))

print("\nTEST 2: Read file")

print(read_file("sample"))

print("\nTEST 3: Invalid filename")

print(create_file("../test", "Invalid file"))

print("\nTEST 4: Missing file")

print(read_file("unknown_file"))
