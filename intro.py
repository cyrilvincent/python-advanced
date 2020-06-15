

def isEven(x):
    return x % 2 == 0

def isGreaterThan(x):
    return x > 5

toto = isEven

def verify(x, verificationFn):
    return verificationFn(x)

def filterByFn(fn, l):
    res = []
    for val in l:
        if fn(val):
            res.append(val)
    return res


def isPrime(x:int=0) -> bool:
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True

# def toto(*params):
#     for p in params:
#         print(p)

# def titi(**kwargs):
#     for p in kwargs:
#         print(p)
#
# toto()
# toto(1)
# toto(1,2,3,4,5,6,74,8,9)
# titi(param1=12, param2=25)

# f(x) = x + 1
f = lambda x : x + 1
isEven = lambda x : x % 2 == 0

def inc(x):
    return x + 1

print(f(3))


