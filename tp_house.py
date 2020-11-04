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

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_filtre, loyers_filtre)
print(slope, intercept, rvalue, pvalue, stderr)

f = lambda x : slope * x + intercept
plt.plot(range(180), f(range(180)), color="red")

plt.show()