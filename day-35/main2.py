import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

account_sid = ""
auth_token = ""

weather_params = {
    "lat": -2.529450,
    "lon": -44.296950,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for weather in weather_data["list"]:
    forecast = weather["weather"][0]["id"]
    if forecast < 700:
        will_rain = True
        break

if will_rain:
    print("Bring an Umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an Umbrella! ☂️",
        from_="+",
        to="+"
    )
    print(message.status)