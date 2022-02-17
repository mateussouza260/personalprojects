import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Getting yesterday´s date and the day before
yesterday = dt.datetime.now() - dt.timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")
day_before = dt.datetime.now() - dt.timedelta(days=2)
day_before = day_before.strftime("%Y-%m-%d")

# Connecting with the stock API
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "34K09FEU86R5CTZ8",
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
stock_data = response.json()


# Calculating variation between the last two days
stock_data_yesterday = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
stock_data_day_before = float(stock_data["Time Series (Daily)"][day_before]["4. close"])
variation = ((stock_data_yesterday / stock_data_day_before) * 100) - 100
if abs(variation) > 5:
    print("Get News")
if variation > 0:
    variation = f"🔺{round(variation, 2)}%"
else:
    variation = f"🔻{round(variation, 2)}%"


# Connecting to the news API
parameters = {
    "apiKey": "1c6643354aa04c309a0a88e3e486f915",
    "q": COMPANY_NAME,
    "from": yesterday,
    "to": yesterday,
    "pageSize": 3,
}
response = requests.get("https://newsapi.org/v2/everything", params=parameters)
response.raise_for_status()
news_data = response.json()
articles = news_data["articles"]

# Formatting the message
message = f"{variation}\n"
for n in range(0, 3):
    title = articles[n]["title"]
    description = articles[n]["description"]
    message += f"Headline: {title}\n Brief: {description}\n"

print(message)

# Connecting with the Tulio API to send SMS

account_sid = "ACaa622bdc6142497cea06dbb982ec0a13"
auth_token = "137ab192d0b383f5d9a4d96c25244cbe"

client = Client(account_sid, auth_token)
to_send = client.messages.create(
    body=message,
    from_="+18304980872",
    to="+5511972736830",
)
print(to_send.status)
