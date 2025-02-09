import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241026.csv")

fur = data["Primary Fur Color"]
gray_fur = data[data["Primary Fur Color"] == 'Gray']
red_fur = data[data["Primary Fur Color"] == 'Cinnamon']
black_fur = data[data["Primary Fur Color"] == 'Black']

print(gray_fur["Hectare Squirrel Number"].sum())


# new_frame = pd.DataFrame(
#     {
#         "Fur Color": ["Cinnamon", "Gray", "Black"],
#         "Count": [
#             fur_list.count("Cinnamon"),
#             fur_list.count("Gray"),
#             fur_list.count("Black"),
#         ],
#     },
# )
# new_frame.to_csv("new.csv")

# print(new_frame.size)
#

squirrel_df = pd.DataFrame({
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_fur['Primary Fur Color'].count(), red_fur['Primary Fur Color'].count(), black_fur['Primary Fur Color'].count()]
})

print(gray_fur.count())
squirrel_df.to_csv('new.csv')
