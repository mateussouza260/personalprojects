import requests
from datetime import datetime

MY_MOCK_LAT = -22.753431
MY_MOCK_LNG = -46.605105

parameters = {
    "lat": MY_MOCK_LAT,
    "lng": MY_MOCK_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
