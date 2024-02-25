import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_URL = os.environ["SHEETY_URL"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": input("Tell me which exercise you did: ")
}

nutritionix_endpoint = "https://trackapi.nutritionix.com"
natural_language_endpoint = f"/v2/natural/exercise"
url = f"{nutritionix_endpoint}{natural_language_endpoint}"

response = requests.post(url=url, json=params, headers=headers)
data = response.json()

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    body = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_URL, json=body, headers=sheety_headers)