#pip install scikit-learn
import sklearn.linear_model
import pandas
import matplotlib.pyplot as plt
import numpy as np

dataframe = pandas.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 200]
plt.scatter(dataframe["surface"], dataframe.loyer)

model = sklearn.linear_model.LinearRegression() # f(x) = ax + b
model.fit(dataframe.surface.values.reshape(-1, 1), dataframe.loyer)

res = model.predict(np.arange(400).reshape(-1, 1))
plt.plot(np.arange(400), res, color="red")
plt.show()
print(f"f(x)={model.coef_}x+{model.intercept_}")

