from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # data = (data - mean) / std
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(30,30,30), max_iter=10000,warm_start=True)
mlp.fit(X_train,y_train)
import pickle
with open("mlp.pickle","wb") as f:
    pickle.dump(mlp, f)
mlp = None
with open("mlp.pickle","rb") as f:
    mlp = pickle.load(f)
predictions = mlp.predict(X_test)


print(y_test - predictions)
print(mlp.score(X_test, y_test))