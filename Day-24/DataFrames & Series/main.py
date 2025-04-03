import pandas as pd
# from numpy import average

data = pd.read_csv("weather_data.csv")
file = data.to_dict()
print(file)

temp = data["temp"].to_list()
print(temp)

# print(average(temp))
print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)

f  = (monday.temp *(9/5))+32
print(f)

data_dict = {
    "student": ["Amy", "James", "Angela" ],
    "Scores":[76, 65, 68 ]
}

data_2 = pd.DataFrame(data_dict)
print(data_2)
data_2.to_csv("new_data.csv")