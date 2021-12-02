from typing import List, Iterable, Generator
import mylib

def myfilter_dirty(fn, l: List[int]):
    res = []
    for nb in l:
        if fn(nb):
            res.append(nb)
    return res

def filter(fn, l: Iterable[int]):
    for nb in l:
        if fn(nb):
            yield nb

def map(fn, l: Iterable[int]):
    for nb in l:
        yield fn(nb)

def list(g: Generator):
    res = []
    for i in g:
        res.append(i)

def infinite():
    i = 0
    while True:
        yield i
        i += 1

if __name__ == '__main__':
    l = range(10000000000000000000000000000000000000000)
    res = filter(lambda x: mylib.is_prime(x), l)
    res = filter(lambda x: x % 2 == 0, res)

    for i in res:
        print(i)
