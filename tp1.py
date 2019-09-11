import math

l = range(2000)
# Diviser tous les chiffres par 1000
# Appliquer un math.sin
# Filtrer les résulats > 0

def div1000(x):
    return x / 1000

def isPositive(x):
    return x > 0

res = map(div1000, l)
res = map(math.sin, res)
res = filter(isPositive, res)
print(list(res))