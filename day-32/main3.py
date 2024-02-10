import datetime as dt
import random
import smtplib

now = dt.datetime.now()
current_date = now.weekday()

if current_date == 3:
    with open("quotes.txt") as file:
        quotes = file.read().splitlines()

    quote = random.choice(quotes)

    my_email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="erick.ap.silva@gmail.com",
                            msg=f"Subject:Hello\n\n{quote}"
        )