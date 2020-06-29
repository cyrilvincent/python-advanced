import unittest

def isEven(x: int) -> bool:
    return x % 2 == 0

def isPrime(x: int) -> bool:
    if x < 2:
        return False
    else:
        for div in range(2,x):
            if x % div == 0:
                return False
        return True

class TP1Test(unittest.TestCase):

    def testIsEven(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(7))

    def testIsPrime(self):
        self.assertTrue(isPrime(7))
        self.assertFalse(isPrime(8))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(524287))
