import tp1
import time

def my_filter(fn, l):
    for i in l:
        if fn(i):
            yield i

def my_map(fn, l):
    for i in l:
        yield fn(i)

def my_range(nb):
    i = 0
    while(i < nb):
        yield i
        i += 1

l = my_range(10)
res = my_filter(lambda x : x % 2 == 0, l)
res2 = my_map(lambda x : x ** 2, res)
print(res2)
print(len(res2))
for i in res2:
    print(i)


def infinite_generator():
    i = 0
    while True:
        yield i
        time.sleep(1)
        i += 1

res = infinite_generator()
res = filter(lambda x : tp1.is_prime(x), res)
res = filter(lambda x : x % 2 == 0, res)
for i in res:
    print(i)

def my_list(g):
    res = []
    for i in g:
        res.append(i)
    return res

l = range(10)
res = filter(lambda x : x % 2 == 0, l)
res = map(lambda x : x ** 2, res)
res = list(res)
#<=>
res = [x ** 2 for x in l if x % 2 == 0] # list + map + filter
#<=>
res = list((x ** 2 for x in l if x % 2 == 0))


l = range(10)
res = filter(lambda x : x % 2 == 0, l)
res = map(lambda x : x ** 2, res)
#<=>
res = (x ** 2 for x in l if x % 2 == 0) # map + filter



