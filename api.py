import requests
import os
from dotenv import load_dotenv

# Read .env file
load_dotenv()

# API settings
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Parameters to send to API
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    # Send request
    response = requests.get(BASE_URL, params=params)

    # Return data if successful
    if response.status_code == 200:
        return response.json()
    else:
        return None