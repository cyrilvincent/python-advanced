import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
# pip install openpyxl

dataframe = pd.read_excel("data/house/house.xlsx")
dataframe = dataframe[dataframe.surface < 200]
dataframe.to_csv("data/house/filtered.csv", index=None)
print(dataframe.describe())

slope, intercept, rvalue,_,_ = stats.linregress(dataframe.surface, dataframe.loyer)
print(f"Correlation: {rvalue*100:.1f}%")

f = lambda x: slope * x + intercept

plt.scatter(dataframe.surface, dataframe.loyer)
x = np.arange(200)
plt.plot(x, f(x), color="red")
plt.show()
