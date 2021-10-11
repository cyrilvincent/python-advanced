from typing import List
import mylib

def filter_even(l:List[int]):
    res = []
    for val in l:
        if val % 2 == 0:
            res.append(val)
    return res

def filter_prime(l:List[int]):
    res = []
    for val in l:
        if mylib.is_prime(val):
            res.append(val)
    return res

def filter_lambda(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res

print(filter_even([1,2,3,4,5,6,7]))
print(filter_prime([1,2,3,4,5,6,7]))
print(filter_lambda(lambda x: x % 2 == 0, [1,2,3,4,5,6,7]))
print(filter_lambda(mylib.is_even, [1,2,3,4,5,6,7]))
print(filter_lambda(lambda x: mylib.is_prime(x), [1,2,3,4,5,6,7]))
# res = filter_lambda(lambda x: mylib.is_prime(x), filter_lambda(lambda x: x % 2 == 0, range(100000000000)))
# for val in res:
#     print(val)

print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7])))
res = filter(lambda x: mylib.is_prime(x), filter(lambda x: x % 2 == 0, range(1000000000000000000)))
res2 = map(lambda x: x ** 0.5, res)
for val in res2:
    print(val)

print(list(map(lambda x: x * 2, range(10))))