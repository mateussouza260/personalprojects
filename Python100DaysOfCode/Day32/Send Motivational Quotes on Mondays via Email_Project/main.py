# import smtplib
#
# my_mock_email = "felipe.barros2600@gmail.com"
# my_mock_password = "abcd1234"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # This enables encryption to the email along the way (making connection secure)
#     connection.login(user=my_mock_email, password=my_mock_password)
#     connection.sendmail(
#         from_addr=my_mock_email,
#         to_addrs="felipebarros2600@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2021, month=5, day=3, hour=20)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt") as quotes:
        df_quotes = quotes.readlines()
        day_quote = random.choice(df_quotes)

my_mock_email = "felipe.barros2600@gmail.com"
my_mock_password = "felipebarros01"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # This enables encryption to the email along the way (making connection secure)
    connection.login(user=my_mock_email, password=my_mock_password)
    connection.sendmail(
        from_addr=my_mock_email,
        to_addrs="felipebarros2600@yahoo.com",
        msg=f"Subject:Monday Motivation\n\n{day_quote}"
    )

