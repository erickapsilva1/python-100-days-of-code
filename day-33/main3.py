import requests, datetime

MY_LAT = -23.744656
MY_LNG = -46.795132
TIME_ZONE = "America/Sao_Paulo"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": TIME_ZONE,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.date
