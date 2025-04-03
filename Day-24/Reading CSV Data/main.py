# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as file:
#     contents = csv.reader(file)
#     temp =[]
#     for i in contents:
#         if i[1] != "temp":
#             temp.append(int(i[1]))
#     print(temp)


import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data["temp"])