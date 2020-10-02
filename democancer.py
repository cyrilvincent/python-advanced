from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']

print(X.shape) #569 * 30
print(y.shape) #569

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)

import sklearn.preprocessing as pp
scaler = pp.StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

import sklearn.neural_network
model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(30,15), max_iter=10000)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
#print(model.coefs_)