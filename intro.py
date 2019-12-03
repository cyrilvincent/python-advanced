def isEven(i):
    return i % 2 == 0

isEvenLambda = lambda i : i % 2 == 0

def isPrime(i):
    if i < 2:
        res = False
    else:
        res = True
        for x in range(2, i):
            if i % x == 0:
                res = False
                break
    return res

def getPrimes(nb):
    res = []
    for i in range(2, nb):
       if isPrime(i):
           res.append(i)
    return res

def filterByPrime(l):
    res = []
    for i in l:
        if isPrime(i):
            res.append(i)
    return res

def filter2(fn, l):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res



import unittest
class MyTest(unittest.TestCase):

    def testFirst(self):
        self.assertEqual(2, 1 + 1)

    def testEven(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(7))

    def testPrime(self):
        self.assertTrue(isPrime(4391))
        self.assertFalse(isPrime(4393))

    def testLambda(self):
        self.assertTrue(isEvenLambda(8))
        self.assertFalse(isEvenLambda(7))

    def testGetPrimes(self):
        l = getPrimes(100)
        print(l)
        self.assertTrue(len(l) > 0)
        l = filterByPrime(range(2,100))
        print(l)
        self.assertTrue(len(l) > 0)
        l = filter2(isPrime, range(2, 100))
        print(l)
        self.assertTrue(len(l) > 0)
        l = filter2(isEven, range(2, 100))
        print(l)
        self.assertTrue(len(l) > 0)
        l = filter2(lambda x : x % 3 == 0, range(100))
        print(list(filter(lambda x : x % 3 == 0, range(1000))))

        print(list(map(lambda x : x ** 2, l)))



if __name__ == '__main__':
    unittest.main()





