import requests
from datetime import datetime as dt

X_APP_ID = "c4c74f2a"

X_APP_KEY = "52535052fc069f82da5966abaf65baf9"

TODAY = dt.now()
GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 183
AGE = 20
QUERY = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/d69a929c9b971204160c4f97595b833c/workoutTracking/workouts"

headers = {
    "Content-Type": "application/json",
    "x-app-id": X_APP_ID,
    "x-app-key": X_APP_KEY,
}


body = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=body)
print(response.text)
data = response.json()["exercises"]


for exercise in data:
    print(exercise["duration_min"])
    sheet_inputs = {
        "workout": {
            "date": TODAY.strftime("%d/%m/%Y"),
            "time": TODAY.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheet_inputs)
    print(response.text)
