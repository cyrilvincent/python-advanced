import numpy as np
import pandas as pd

a1 = np.array([1,2,3,4])
print(a1)
a2 = np.arange(4)
print(a2)
print(a1 * a2)
print(np.sqrt(a1))
print(np.sin(a1))
print(np.sqrt(a1) * np.sin(a2))

print(a1.ndim, a1.size, a1.shape)

rnd = np.random.rand(1000)
print(rnd)
print(len(rnd[rnd > 0.5]))

dataframe = pd.read_csv("data/house/house.csv")
loyer_m2 = dataframe.loyer / dataframe.surface
dataframe["loyer_m2"] = loyer_m2

print(dataframe.describe())
dataframe.to_excel("data/house/house2.xlsx")

np.savez("data/file.npz", a1 = a1, a2 = a2)
data = np.load("data/file.npz")
a1 = data["a1"]
a2 = data["a2"]
print(a1, a2)