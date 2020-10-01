import demo

def filter(fn, l):
    for i in l:
        if fn(i):
            yield i #return streaming

def map(fn, l):
    for i in l:
        yield fn(i)

def range(x):
    i = 0
    while i < x:
        yield i
        i+=1

def list(g):
    res = []
    for i in g:
        res.append(i)
    return res

res = filter(lambda x : x % 2 == 0, range(10)) #Generator hérite d'un Iterator
res = map(lambda x : x ** 2, res)
#print(res[2])
#<=>
res = (x ** 2 for x in range(10) if x % 2 == 0)

res = list((x ** 2 for x in range(10) if x % 2 == 0))
#<=>
res = [x ** 2 for x in range(10) if x % 2 == 0]
print(res[2])

#print(len(res))
for val in res:
    print(val)
print("Fin generateur 1")
for val in res:
    print(val)
print("Fin generateur 2")

def inifinite():
    i = 0
    while True:
        yield i
        i += 1

generator = filter(lambda x : demo.is_prime(x), inifinite())
generator = filter(lambda x : x % 2 == 0, generator)
for i in generator:
    print(i)




