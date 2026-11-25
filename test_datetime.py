from tools.datetime_tool import get_datetime

result = get_datetime()

print("Current Date and Time:")
print("Date:", result["date"])
print("Time:", result["time"])
print("Day:", result["day"])
