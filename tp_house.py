import csv
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
    loyers = np.array([float(row["loyer"]) for row in reader])
    surfaces = np.array([float(row["surface"]) for row in reader])

surfaces_filtre = surfaces[surfaces < 180.0]
loyers_filtre = loyers[surfaces < 180.0]

plt.scatter(surfaces_filtre, loyers_filtre)

res = stats.linregress(surfaces_filtre, loyers_filtre)
print(res[0], res[1], res[2], res[3])

f = lambda x : res[0] * x + res[1]
plt.plot(surfaces_filtre, surfaces_filtre * res[0] + res[1], color="red")

plt.show()