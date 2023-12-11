import math

l = [1,2,8,7,9,12,13,99,51,11]

res = [x * 2 for x in l]
print(res)

res = [x for x in l if x % 2 == 0]
print(res)

res = [math.sqrt(x) for x in l if x % 2 == 0]
print(res)

def add(i, j):
    return i + j

toto = add
print(type(toto))
print(toto(2,3))
