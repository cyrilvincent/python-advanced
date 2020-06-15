

def isEven(x):
    return x % 2 == 0

def isPrime(x):
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True


