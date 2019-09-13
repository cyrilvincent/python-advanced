import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import sqlite3

with sqlite3.connect("house/house.db3") as conn:
    data = pd.read_sql('select loyer,surface from house where surface < 250', conn)

#data = pd.read_csv("house/house.csv")
#data = data[data.surface < 250]
surfaces =data["surface"]
loyers =data["loyer"]

slope, intercept, _,_,_ = scipy.stats.linregress(surfaces, loyers)

plt.plot(range(250), [slope * x + intercept for x in range(250)])

plt.scatter(surfaces, loyers)
plt.show()