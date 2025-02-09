OWM_Endpoint = ""
api_key = ""
import os
from dotenv import load_dotenv

load_dotenv()

weather_params = {
    "lat":1,
    "lon": 2,
    "appid": api_key,
    "cnt": 4
}

import requests

os.environ.get("")

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
