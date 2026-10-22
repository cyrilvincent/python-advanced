import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("data/house/house.csv")
print(df)
print(df.dtypes)
df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
print(np.mean(df["loyer_m2"]))
print(np.median(df["loyer_m2"]))
print(np.std(df["loyer_m2"]))
print(np.mean(df["loyer"]))
print(np.median(df["loyer"]))
print(np.std(df["loyer"]))
df.to_excel("data/house/house.xlsx", index=False)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(df["surface"], df["loyer"])
print(slope, intercept, rvalue, pvalue)
x = np.arange(400)
y = slope * x + intercept

plt.subplot(2,1,1)
plt.scatter(df["surface"], df["loyer"], label="loyers", color="red")
plt.title("Surface / Loyer à paris")
plt.legend()
plt.plot(x, y)
plt.subplot(2,1,2)
plt.hist(df["loyer"], bins=20)
plt.show()

