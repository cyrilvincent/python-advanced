import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("data/house/house.csv")
df = df[df.surface < 200]
df = df[df.loyer < 20000]
# df = pd.read_excel("data/house/house.xlsx")
df["loyer_per_m2"] = df.loyer / df.surface
print(df.head())
print(df.describe())
df.to_json("data/house/house.json")

fsin = [math.fabs(math.sin(x / 100) * 8000) for x in range(0 ,628)]
plt.subplot(1,2,1)
plt.plot(range(0,628), fsin, "red")
plt.subplot(1,2,2)
plt.scatter(df.surface, df.loyer)
plt.show()
