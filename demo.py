def is_prime(x):
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
    return True

def filter_even(l):
    res = []
    for i in l:
        if i % 2 == 0:
            res.append(i)
    return res

def myfilter(fn, l):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def mymap(fn, l):
    res = []
    for i in l:
        res.append(fn(i))
    return res

def double(x):
    return x * 2

def inc(x):
    return x + 1

def demo_tuple():
    #Calcul
    a = 1
    b = 99
    return a,b




# Reprise 10h35
