x = 1
print(type(x))

y = "toto"

def add(i,j):
    return i + j

z = add

print(type(z))

print(z(1,2))

import intro
res = filter(intro.isPrime, range(100))
print(list(res))
