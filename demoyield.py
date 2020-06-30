import tp1
from typing import *

def infinite():
    i = 0
    while True:
        yield i
        i+=1

def range(end):
    i = 0
    while i < end:
        yield i
        i+=1

l = range(100000000000000)
l = infinite()

def filter(fn, l:Iterator):
    #res = []
    for val in l:
        if fn(val):
            yield val
            #res.append(val)
    #return res

def map(fn, l):
    for val in l:
        yield fn(val)

def list(generator):
    res = []
    for val in generator:
        res.append(val)
    return res

# res = list(filter(tp1.isPrime, l))
# res = [x for x in l if tp1.isPrime(x)]

res = filter(tp1.isPrime, l)
res = map(lambda x : x **2, res)
res = filter(lambda x : x % 2 == 0, res)
# Sequentiel
#res = list(res)
# Boucler qu'une fois
#print(len(res))

for val in res:
    print(val)