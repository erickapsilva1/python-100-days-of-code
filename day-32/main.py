import smtplib

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="erick.ap.silva@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email"
    )
