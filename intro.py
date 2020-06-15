

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


