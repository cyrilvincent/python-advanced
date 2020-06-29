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

f = lambda x : x + 1

class TP1Test(unittest.TestCase):

    def testIsEven(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(7))

    def testIsPrime(self):
        self.assertTrue(isPrime(7))
        self.assertFalse(isPrime(8))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(524287))

    def testLambda(self):
        self.assertEqual(2, f(1))

    def testFilter(self):
        l = [1,2,3,4,5,6,7,8,9]
        self.assertListEqual([2,4,6,8], myfilter(isEven, l))
        self.assertListEqual([2,3,5,7], myfilter(isPrime, l))
        self.assertListEqual([2,4,6,8], myfilter(lambda x : x % 2 == 0, l))
        self.assertListEqual([2, 3, 5, 7], myfilter(lambda x : isPrime(x), l))
