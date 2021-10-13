import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import sklearn.model_selection as ms

dataframe = pd.read_csv("data/house/house.csv")
dataframe_filter = dataframe[dataframe.surface < 200]

y = dataframe_filter.loyer
x = dataframe_filter.surface.values.reshape(-1, 1)
print(dataframe_filter.surface.shape)
print(x.shape)

#model = lm.LinearRegression()
model = pipe.make_pipeline(pp.PolynomialFeatures(3), lm.Ridge())
model.fit(x, y)
#print(model.coef_, model.intercept_)

predict = model.predict(np.arange(200).reshape(-1, 1))
print(model.score(x, y))

plt.scatter(dataframe_filter.surface, dataframe_filter.loyer)
plt.plot(np.arange(200), predict, color='red')
plt.show()
