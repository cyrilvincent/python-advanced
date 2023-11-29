import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.describe())
dataframe = dataframe[dataframe.surface < 200]
dataframe2 = pd.read_excel("data/house/house.xlsx")
print(dataframe2.T)

res = dataframe.surface - dataframe2.surface
print(res[res!=0])

slope, intercept, rvalue, pvalue, mse = scipy.stats.linregress(dataframe.surface, dataframe.loyer)
print(slope, intercept, rvalue, pvalue, mse)

x = np.arange(200)
y = slope * x + intercept

plt.scatter(dataframe.surface, dataframe.loyer)
plt.plot(x, y, "red")
plt.show()


