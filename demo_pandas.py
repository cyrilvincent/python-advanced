import pandas as pd
# pip install xlrd

dataframe = pd.read_excel("data/house/house.xlsx")
dataframe = dataframe[dataframe.surface < 200]
dataframe.to_csv("data/house/filtered.csv", index=None)
print(dataframe)
print(dataframe.surface)