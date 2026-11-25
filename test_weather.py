
from tools.weather import get_weather

print("TEST 1: Valid city")

print(get_weather("Hyderabad"))

print("\nTEST 2: Invalid city")

print(get_weather("invalidxyzcity"))

print("\nTEST 3: Empty city")

print(get_weather(""))
