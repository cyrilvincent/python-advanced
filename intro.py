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

def filterPrime(l):
    res = []
    for i in l:
        if isPrime(i):
            res.append(i)
    return res

def filter2(predicatFn, l):
    res = []
    for i in l:
        if predicatFn(i):
            res.append(i)
    return res

def map2(mapFn, l):
    res = []
    for i in l:
        res.append(mapFn(i))
    return res

def double(x):
    return x * 2

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

    def testFilterPrime(self):
        l=range(10)
        self.assertListEqual([2,3,5,7], filterPrime(l))

    def testFilterEvenAndPrime(self):
        l=range(10)
        res = filterPrime(l)
        self.assertListEqual([2], filterEven(res))

    def testAffectFunction(self):
        x = isEven
        self.assertTrue(x(2))

    def testFilterPredicate(self):
        l=range(10)
        self.assertListEqual([0,2,4,6,8], filter2(isEven, l))
        self.assertListEqual([2,3,5,7], filter2(isPrime, l))

    def testFilter(self):
        l=range(10)
        self.assertListEqual([0,2,4,6,8], list(filter(isEven, l)))
        self.assertListEqual([2,3,5,7], list(filter(isPrime, l)))

    def testHugeFilter2(self):
        l=range(100)
        self.assertListEqual([2], filter2(isEven, filter2(isPrime, l)))

    def testMap2(self):
        l = range(5)
        self.assertListEqual([0,2,4,6,8], map2(double, l))

    def testMap(self):
        l = range(5)
        self.assertListEqual([0,2,4,6,8], list(map(double, l)))

if __name__ == '__main__':
    unittest.main()


    