import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as sklm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe

df = pd.read_csv("house/house.csv")
x = df["surface"].values.reshape(-1,1)
y = df["loyer"]
model = sklm.LinearRegression()
model.fit(x,y)
print(f"Score: {model.score(x,y)}")
print(model.coef_, model.intercept_)

plt.scatter(x,y)
plt.scatter(x, model.predict(x))

x = df["surface"].values.reshape(-1,1)
y = df["loyer"]
model = pipe.make_pipeline(pp.PolynomialFeatures(3), sklm.Ridge())
model.fit(x,y)
print(f"Score: {model.score(x,y)}")
plt.scatter(x, model.predict(x))

plt.show()