weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def c_to_f(temp_c):
    return (temp_c * 9/5) + 32


weather_f = {day: c_to_f(temp) for (day, temp) in weather_c.items()}
print(weather_f)
