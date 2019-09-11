import unittest
import math

def isEven(x:int):
    return x % 2 == 0

def isPrime(x:int):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def filterEven(l):
    res = []
    for i in l:
        if isEven(i):
            res.append(i)
    return res

class MyTests(unittest.TestCase):

    def testFirst(self):
        self.assertEqual(2, 1+1)

    def testIsEven(self):
        self.assertTrue(isEven(2))
        self.assertFalse(isEven(3))

    def testIsPrime(self):
        self.assertTrue(isPrime(7))
        self.assertFalse(isPrime(8))

    def testFilterEven(self):
        l=range(10)
        self.assertListEqual([0,2,4,6,8], filterEven(l))

if __name__ == '__main__':
    unittest.main()
    