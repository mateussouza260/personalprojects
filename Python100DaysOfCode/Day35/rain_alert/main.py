import requests
from twilio.rest import Client

api_key = "0bedbbeaa3c781343feccd445449d4ad"
account_sid = "ACaa622bdc6142497cea06dbb982ec0a13"
auth_token = "137ab192d0b383f5d9a4d96c25244cbe"


mock_latitude = -22.783621
mock_longitude = -46.561352

parameters = {
    "lat": mock_latitude,
    "lon": mock_longitude,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

connection = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
connection.raise_for_status()
weather_data = connection.json()
hourly_data = [weather_data["hourly"][h]["weather"][0]["id"] for h in range(0, 12)]

will_rain = False

for h in hourly_data:
    if h < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        # body="It´s going to rain today! Bring an umbrella ☔",
        body="Você tem o filho mais lindo do mundo\n-Mateus",
        from_="+18304980872",
        to="+5511995314217",
    )
    print(message.status)

