import pandas as pd

dataframe = pd.read_excel("data/house/house.xlsx")
print(dataframe.describe())
dataframe.to_xml("data/house/house.xml")
