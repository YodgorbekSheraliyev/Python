import csv

with open("./weather.csv", ) as data_file:
    temp_list = list()
    data = csv.reader(data_file)
    for row in data:
        if row[0] == 'day':
            continue
        temp_list.append(int(row[1]))

print(temp_list)
