l = range(100)

def is_prime(x):
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
    return True
