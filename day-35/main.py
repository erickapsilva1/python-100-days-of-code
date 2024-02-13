import requests
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

weather_params = {
    "lat": -2.529450,
    "lon": -44.296950,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

for weather in weather_data["list"]:
    forecast = weather["weather"][0]["id"]
    if forecast < 700:
        print("Bring an Umbrella!")
        break
