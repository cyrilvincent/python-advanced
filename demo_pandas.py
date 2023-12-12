import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/house/house.csv")
df = df[df.surface < 200]
df = df[df.loyer < 20000]
# df = pd.read_excel("data/house/house.xlsx")
df["loyer_per_m2"] = df.loyer / df.surface
print(df.head())
print(df.describe())
df.to_json("data/house/house.json")

plt.scatter(df.surface, df.loyer)
plt.show()
