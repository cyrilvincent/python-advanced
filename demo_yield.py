import mylib

# eval("print('toto')")

def filter(fn, l):
    for val in l:
        if fn(val):
            yield val

def map(fn ,l):
    for val in l:
        yield fn(val)

def range(max):
    i = 0
    while i < max:
        yield i
        i += 1

def list(g):
    res = []
    for val in g:
        res.append(val)
    return res

def infinite():
    i = 0
    while True:
        yield i
        i += 1
        
res = filter(lambda x: x % 2 == 0, range(10))
res = filter(lambda x: mylib.is_prime(x), res)
res = map(lambda x: x ** 0.5, res)
print(len(list(res)))
for val in res:
    print(val)

# filter
res = filter(lambda x: x % 2 == 0, range(10))
# <=> generator
res = (x for x in range(10) if x % 2 == 0)

# map
res = map(lambda x: x ** 0.5, range(10))
# <=> generator
res = (x ** 0.5 for x in range(10))

# map + filter
res = map(lambda x: x ** 0.5, filter(lambda x: mylib.is_prime(x), range(100)))
# <=> generator
res = (x ** 0.5
       for x in range(100)
       if mylib.is_prime(x))
print(list(res))
print(list((x ** 0.5 for x in range(100) if mylib.is_prime(x))))

# Intention list <=> Comprehension
res = list((x ** 0.5 for x in range(100) if mylib.is_prime(x)))
# <=>
res = [x ** 0.5 for x in range(100) if mylib.is_prime(x)]

