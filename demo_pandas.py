import pandas as pd
import matplotlib.pyplot as plt

#dataframe = pd.read_csv("data/house/house.csv")
dataframe = pd.read_excel("data/house/house.xlsx",sheet_name=0)
print(dataframe[dataframe.surface < 180])
print(dataframe.loyer / dataframe.surface)

plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()

dataframe2 = dataframe[dataframe.surface < 180]
dataframe2.to_csv("data/house/house180.csv",index=False)