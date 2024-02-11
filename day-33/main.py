import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)

response.raise_for_status()
data = response.json()
print(data)

data = response.json()["iss_position"]
print(data)

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)
