import matplotlib.pyplot as plt
import pandas as pd

yearly_df = pd.read_csv('./annual_deaths_by_clinic.csv')

plt.plot(yearly_df.year, yearly_df.births)
plt.show()
