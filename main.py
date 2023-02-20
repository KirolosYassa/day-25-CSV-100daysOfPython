# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# content = []
#
# for line in data:
#     new_line = line.replace("\n", "")
#     content.append(new_line)
# print(content)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[0].index("day") == 0:
#             continue
#         temperature.append(row[1])
# print(temperature)

#
# data = pandas.read_csv("weather_data.csv")
#
# max_temp = data["temp"].max()
# # print(max_temp)
# monday = data[data.day == "Monday"]
# cels = monday.temp
# fahr = (cels * 9.0/5.0) + 32.0
# print(int(fahr))
#
# data_dict = {
#     "students": ["Kirolos", "Mina", "Nonos"],
#     "scores": [50, 30, 80]
# }
#
# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("Central_Park-Squirrel_Data.csv")
# print(data)
gray = len(data[data["Primary Fur Color"] == "Gray"])
# print(len(gray))
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(len(cinnamon))
black = len(data[data["Primary Fur Color"] == "Black"])
# print(len(black))

new_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
new_data = pandas.DataFrame(new_dict)
# print(new_data)
new_data.to_csv("squirrel_count.csv")