import numpy as np

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([-1,-1,-1,1]) # 0 center

import sklearn.neural_network
model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(4,8), max_iter=1000)

model.fit(X, y)

res = model.predict(X)
print(res)
print(res > 0)

