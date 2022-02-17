# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#
# print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

complete_df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df_primary = complete_df["Primary Fur Color"]
print(df_primary)
df_primary = df_primary.value_counts()
df_primary.to_csv("squirrel_count.csv")

