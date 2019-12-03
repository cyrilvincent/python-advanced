import intro

def filter(fn, l):
    for i in l:
        if fn(i):
           yield i

def map(fn, l):
    for i in l:
        yield fn(i)

def range(nb):
    i = 0
    while i < nb:
        yield i
        i += 1

l = range(100)
res = filter(intro.isPrime, l)
res = filter(lambda x : x %2 == 0, res)
res = map(lambda x : x + 1, res)
for i in res:
    print(i)

res = filter(intro.isPrime, l)
# <=> Generator
res = (x for x in l if intro.isPrime(x))

res = list((x for x in l if intro.isPrime(x)))
#<=> Intention list
res = [x for x in l if intro.isPrime(x)]
