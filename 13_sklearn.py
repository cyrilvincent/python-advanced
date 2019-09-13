import pandas as pd
import sklearn.linear_model as sklm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.model_selection as ms


data = pd.read_csv("house/house.csv")
data = data[data.surface < 250]
surfaces =data["surface"].values.reshape(-1,1)
loyers =data["loyer"]

xtrain, xtest, ytrain, ytest = ms.train_test_split(surfaces, loyers, train_size=0.8, test_size=0.2)


#model = sklm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(3), sklm.Ridge())
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

import matplotlib.pyplot as plt
import numpy as np
plt.plot(surfaces, loyers, 'ro', markersize=4)
plt.plot(range(250), model.predict(np.arange(250).reshape(-1,1)) )
plt.show()






