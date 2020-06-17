import sklearn.linear_model as lm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
plt.scatter(dataframe.surface, dataframe.loyer)


model = lm.LinearRegression()
model.fit(dataframe.surface.values.reshape(-1, 1), dataframe.loyer)
print(model.coef_, model.intercept_) # f(x) = 41*x - 283

plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1,1)))
plt.show()

