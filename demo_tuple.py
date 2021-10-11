from typing import Tuple, Iterable
import math
import random
import csv

def test_tuple():
    return 1, "toto", 0, "x"

a,b,_,_ = test_tuple()
print(a,b)

# faire la fonction min_max_avg(generator: Iterable[float])->Tuple[float, float, float]
def min_max_avg(generator: Iterable[float])-> Tuple[float, float, float]:
    min = math.inf
    max = -math.inf
    sum = 0
    nb = 0
    for value in generator:
        if value < min:
            min = value
        if value > max:
            max = value
        sum += value
        nb += 1
    return min, max, sum / nb

res = [random.uniform(0,100) for _ in range(1000)]
print(res)
print(min_max_avg(res))

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    surfaces = []
    loyers = []
    for row in reader:
        surfaces.append(float(row["surface"]))
        loyers.append(float(row["loyer"]))

import scipy
print(scipy.__version__)
import scipy.stats as stats
tuple = stats.linregress(surfaces, loyers)
print(tuple)

import matplotlib.pyplot as plt
plt.scatter(surfaces, loyers)
f = lambda x : tuple[0] * x + tuple[1]
plt.plot(surfaces, [f(x) for x in surfaces], color="red")
plt.show()
