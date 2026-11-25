
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):

    if not API_KEY:
        return {"error": "Weather API key not found"}

    if not isinstance(city, str) or not city.strip():
        return {"error": "Please provide a valid city name"}

    try:

        url = "https://api.weatherapi.com/v1/current.json"

        params = {
            "key": API_KEY,
            "q": city.strip(),
            "aqi": "no"
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 400:
            return {"error": "Invalid city name. Please enter a valid city."}

        response.raise_for_status()

        data = response.json()

        weather = {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_kph"]
        }

        return weather

    except requests.exceptions.Timeout:

        return {"error": "Weather request timed out. Please try again."}

    except requests.exceptions.RequestException:

        return {"error": "Unable to connect to the weather service."}

    except (KeyError, ValueError):

        return {"error": "Unable to process weather information."}
