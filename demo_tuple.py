from typing import Tuple, Iterable
import math
import random

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
