import math

l = range(2000)
# Diviser tous les chiffres par 1000
# Appliquer un math.sin
# Filtrer les résulats > 0

def div1000(x):
    return x / 1000

def isPositive(x):
    return x > 0

isPositive = lambda x : x > 0

res = map(lambda x : x / 1000, l)
res = map(lambda x : math.sin(x + math.pi / 3), res)
res = filter(lambda x : x > 0, res)
print(list(res))