

def isEven(x):
    return x % 2 == 0

toto = isEven

def verify(x, verificationFn):
    return verificationFn(x)


def isPrime(x:int=0) -> bool:
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True


def toto(x, tutu,y=0,titi=0):
    pass

