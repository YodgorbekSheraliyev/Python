import pandas as pd

data = pd.read_csv('weather.csv')

# data1 = pd.DataFrame([1,2,3,4,5,6,7,7])
# series = pd.Series(['a', 'a','a','a','a','a','a','a','a','a','a','a'])

# Average temperature
temp = data['temp'].mean()

# Return row where column equals = monday
row = data[data.day == 'Monday']
# print(row)

# Return row where temperatue is maximum
max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)