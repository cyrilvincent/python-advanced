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

X = np.matrix([np.ones(surfaces.shape[0]), surfaces]).T
y = np.matrix(loyers).T

import sklearn.model_selection as ms

xtrain, xtest, ytrain, ytest = ms.train_test_split(X, y, train_size=0.8, test_size=0.2)
print(len(xtrain)/len(xtest))

import sklearn.linear_model as sklm

regr = sklm.LinearRegression()
regr.fit(xtrain,ytrain)
import math
print(1 - math.sqrt( regr.score(xtrain,ytrain))) #9.3%
print(regr.coef_[0][1])
print(regr.intercept_[0])

#print(xtrain.getA().T[1])

import matplotlib.pyplot as plt
plt.plot(xtrain.T[1], ytrain.T[0], 'ro', markersize=4)
plt.plot(xtrain.getA().T[1], regr.predict(xtrain).T[0] )
plt.show()

import matplotlib.pyplot as plt
plt.plot(xtest.T[1], ytest.T[0], 'ro', markersize=4)
plt.plot(xtest.getA().T[1], regr.predict(xtest).T[0] )
plt.show()

import sklearn.metrics as m
print(math.sqrt(m.mean_squared_error(regr.predict(xtest), ytest))) # 537





