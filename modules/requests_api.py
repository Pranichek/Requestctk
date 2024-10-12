import requests
from .read_json import read_json
import json

data_json = read_json(filename= "config_api.json")
API_KEY = data_json['api_key']
NAME_CITY = data_json['city_name']

URL = f"https://api.openweathermap.org/data/2.5/weather?q={NAME_CITY}&appid={API_KEY}"
response = requests.get(URL)

if response.status_code == 200:
    data_weather = json.loads(response.content)
    print(json.dumps(data_weather , indent = 4))
    print(data_weather["weather"][0]["main"])
    print(data_weather["main"]["temp"])
else:
    print(f"Error: {response.status_code}")

