import numpy as np


X = []
y = []
for i in range(8):
    for j in range(8):
        X.append([i,j])
        y.append([i+j])
X=np.array(X, dtype=float)
y=np.array(y, dtype=float)
print(X)
print(y)
X = (X - 3.5) / 3.5 # 0 center
y = (y - 3.5) / 3.5
print(X)
print(y)

import sklearn.neural_network
model = sklearn.neural_network.MLPRegressor(hidden_layer_sizes=(64,32,16), max_iter=10000)
print(X.shape, y.shape)
model.fit(X, y)

res = model.predict(X)
print(res)
for i in range(8):
    for j in range(8):
        predict = int(round(res[i * 8 + j] * 3.5 + 3.5))
        print(f"{i}+{j}={predict} {i+j==predict}")


