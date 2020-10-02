import numpy as np
import pandas
import matplotlib.pyplot as plt

l1 = [1,2,3]
l2 = [4,5,6]
print(l1 + l2)
print(l1 * 2)
a1 = np.array(l1, dtype=bool)
a2 = np.array(l2)
print(a1 + a2)
print(a1 * 2)
print(a1 * a2)
print(np.dot(a1, a2))

m1 = np.array([[1,2],[3,4]])
print(m1 * 2)
m2 = np.array([4,5,6,7]).reshape(2,2)
print(m2)
print(m1.dot(m2))

dataframe = pandas.read_csv("data/house/house.csv")
print(dataframe)
res = dataframe["loyer"] / dataframe.surface
print(np.min(res))
print(np.max(res))
print(np.mean(res))
print(np.std(res))
print(np.median(res))

# Charger house.csv avec pandas
# Calculer pour loyer : min, max, avg, std, median
# Calculer pour loyer / surface : min, max, avg, std, median
# Afficher un schema x = loyer, y = surface

plt.scatter(dataframe["surface"], dataframe.loyer)
plt.show()