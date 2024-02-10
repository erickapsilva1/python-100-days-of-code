##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_data = pandas.read_csv("birthdays.csv")
current_day = dt.datetime.now().day
current_month = dt.datetime.now().month
birthdays_of_the_day = birthdays_data[(birthdays_data["day"] == current_day) & (birthdays_data["month"] == current_month)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

def send_email(to, title, mail_body):
    my_email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to,
                            msg=f"Subject:{title}\n\n{str(mail_body)}"
                            )


for index, row in birthdays_of_the_day.iterrows():
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        title = "Happy Birthday"
        name = row['name']
        to = row['email']
        sender = "Erick"
        letter = str(letter).replace("[NAME]", name)
        letter = str(letter).replace("[SENDER]", sender)

        send_email(to=to, title=title, mail_body=letter)

















