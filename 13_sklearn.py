import csv

data = []
with open("house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        t = (float(row["loyer"]), float(row["surface"]))
        data.append(t)

import numpy as np

surfaces = np.array([d[1] for d in data])
loyers = np.array([d[0] for d in data])

import sklearn.linear_model as sklm

regr = sklm.LinearRegression()
X = np.matrix([np.ones(surfaces.shape[0]), surfaces]).T
print(X)
y = np.matrix(loyers).T
print(y)
regr.fit(X,y)
print(regr.predict(X).T[0])
import math
print(1 - math.sqrt( regr.score(X, y))) #9.3%
print(regr.coef_[0][1])
print(regr.intercept_[0])

import matplotlib.pyplot as plt
plt.plot(surfaces, loyers, 'ro', markersize=4)
plt.plot(surfaces, regr.predict(X).T[0] )
plt.show()






