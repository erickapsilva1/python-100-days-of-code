import requests
import smtplib
from datetime import datetime

MY_LAT = -145.2068
MY_LNG = -18.6747
TIME_ZONE = "America/Sao_Paulo"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": TIME_ZONE,
    "formatted": 0,
}


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    latitude = float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])

    return latitude, longitude


def sunset_sunrise():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset


def is_closed_to_iss_position():
    if MY_LAT-5 <= iss_position()[0] <= MY_LAT+5 and MY_LNG-5 <= iss_position()[1] <= MY_LNG+5:
        return True

    return False


def is_currently_dark():
    cur_hour = datetime.now().hour + 10
    if cur_hour < sunset_sunrise()[0] or cur_hour > sunset_sunrise()[1]:
        return True

    return False


def send_email(to, title, mail_body):
    my_email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to,
                            msg=f"Subject:{title}\n\n{str(mail_body)}"
                            )


if is_currently_dark() and is_currently_dark():
    send_email("erick.ap.silva@gmail.com", "ISS is Visible Now!", "Hey, look up to the sky!")





