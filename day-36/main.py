import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_ENDPOINT_API_KEY = ""
NEWS_ENDPOINT_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_ENDPOINT_API_KEY
}

new_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_ENDPOINT_API_KEY
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
time_series = response.json()["Time Series (Daily)"]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_data = [value for (key, value) in time_series.items()]
yesterday = stock_data[0]
yesterday_price = float(yesterday["4. close"]) # 184.02

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = stock_data[1]
day_before_yesterday_price = float(day_before_yesterday["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
abs_value = abs(yesterday_price - day_before_yesterday_price)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
perc_difference = (abs_value / 100) * float(yesterday_price)
up_down = None
if perc_difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if perc_difference > 0.5:
    print("Get news!")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
response = requests.get(NEWS_ENDPOINT, params=new_params)
response.raise_for_status()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
articles = response.json()["articles"]
three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"{STOCK_NAME}: {up_down}{perc_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+12137861232",
        to="+5511948343716"
    )
    print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

