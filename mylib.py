import math
import logging
from typing import List


def is_even(x):
    return x % 2 == 0


def is_prime(x):
    if x < 2:
        return False
    for div in range(2, int(math.sqrt(x) + 1)):
        logging.info(f"div: {div}")
        if x % div == 0:
            return False
    return True


def sum1(l: List[float]):
    res = 0
    for value in l:
        res += value
    return res

def sum2(*kargs):
    res = 0
    for value in kargs:
        res += value
    return res

def bydict(**kwargs):
    value1 = kwargs["cle1"]
    value2 = kwargs["cle2"]

def alltypeofparameter(a,b,c=0,d=1,*kargs,**kwargs):
    pass
