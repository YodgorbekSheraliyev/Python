import pandas

data = pandas.read_csv('./50_states.csv')

for (index, row) in data.iterrows():
    print(row)