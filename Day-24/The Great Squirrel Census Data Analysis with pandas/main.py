import pandas as pd

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_color = len(data[data["Primary Fur Color"] == "Gray"])
red_color = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color = len(data[data["Primary Fur Color"] == "Black"])
print(grey_color)
print(red_color)
print(black_color)
data_dict= {
    "Fur Color":["Grey", "Cinnamon", "Black"],
    "Count": [grey_color, red_color, black_color]
}
df = pd.DataFrame(data_dict)
file = df.to_csv("Squirrel_count.csv")
data_2 = pd.read_csv("Squirrel_count.csv")
print(data_2)