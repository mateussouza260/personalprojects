##################### Extra Hard Starting Project ######################

import pandas as pd
import datetime as dt
import smtplib

my_mock_email = "felipe.barros2600@gmail.com"
my_mock_password = "felipebarros01"
PLACEHOLDER = "[NAME]"

birthdays = pd.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient="records")

now = dt.datetime.now()
today_month = now.month
today_day = now.day
names = {item["name"]: item["email"] for item in birthdays if item["day"] == today_day and item["month"] == today_month}
print(names)
with open("letter_templates/letter_1.txt") as letter_file:
    letter_content = letter_file.read()
    for key, value in names.items():
        print(key)
        print(value)
        new_letter = letter_content.replace(PLACEHOLDER, key)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # This enables encryption to the email along the way (making connection secure)
            connection.login(user=my_mock_email, password=my_mock_password)
            connection.sendmail(
                from_addr=my_mock_email,
                to_addrs=value,
                msg=f"Subject:Happy Bday!\n\n{new_letter}"
        )
