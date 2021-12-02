import math

def is_prime(nb: int):
    if nb < 2:
        return False
    for div in range(2, int(math.sqrt(nb) + 1)):
        if nb % div == 0:
            return False
    return True