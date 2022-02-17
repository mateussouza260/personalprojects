import requests
from datetime import datetime
import smtplib
from time import time, sleep

MY_LAT = -22.753708
MY_LONG = -46.561352
my_mock_email = "felipe.barros2600@gmail.com"
my_mock_password = "felipebarros01"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def iss_is_close():
    # ISS location data
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data_iss = response.json()
    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    if abs(iss_latitude - parameters["lat"]) < 5 and abs(iss_longitude - parameters["lng"]) < 5:
        return True


def is_night():
    # Sunrise and sunset data
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_sun = response.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if iss_is_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_mock_email, password=my_mock_password)
            connection.sendmail(
                from_addr=my_mock_email,
                to_addrs="mateus-souza2001@uol.com.br",
                msg="Subject:ISS is passing over you!\n\nLook up."
            )
    else:
        print("not close")
    sleep(60)


