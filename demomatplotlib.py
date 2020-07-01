import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

a1 = np.array([1,2,3,4,5])
a2 = np.arange(5)
print(a1 + a2)
print(np.cos(a1) * 2)
print(a1[a1 % 2 == 0])


import csv
with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
    loyers = [float(row["loyer"]) for row in reader]
    surfaces = [float(row["surface"]) for row in reader]
    loyers = np.array(loyers)
    surfaces = np.array(surfaces)

    slope, intercept, rvalue, pvalue, stderr = scipy.stats.linregress(surfaces, loyers)
    f = lambda x : slope * x + intercept
    print(slope, intercept, rvalue)

    plt.scatter(surfaces, loyers)
    x = np.arange(400)
    plt.plot(x, f(x))
    print(np.max(loyers), np.min(loyers), np.mean(loyers), np.std(loyers), np.median(loyers))
    loyersperm2 = loyers / surfaces
    #print(loyersperm2)
    print(np.mean(loyersperm2), np.std(loyersperm2), np.median(loyersperm2))

    plt.show()


