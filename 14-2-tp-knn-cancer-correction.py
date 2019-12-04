from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']

print(X.shape) #569 * 30
print(y.shape) #569

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)

import sklearn.neighbors as nn
bestk = 0
bestscore = 0
for k in range(3, 100):
    model = nn.KNeighborsClassifier(k)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test) #93%
    print(f"k={k} score={score}")
    if score > bestscore:
        bestk = k
        bestscore = score

print(f"Best k={bestk} score={bestscore}")
model = nn.KNeighborsClassifier(bestk)
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print(predicted)
print(y_test)
print(predicted - y_test)