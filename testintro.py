import unittest
import math
import intro

def isEven():
    pass

class MyTests(unittest.TestCase):

    def testFirst(self):
        self.assertEqual(2, 1+1)

    def testIsEven(self):
        res = intro.isEven(8)
        self.assertEqual(True, res)
        self.assertEqual(False, isEven(7))

    def testAlmostEqual(self):
        self.assertAlmostEqual(3.14, math.pi, delta=1e-2)
        self.assertAlmostEqual(2, math.sqrt(2) ** 2, delta=1e-5)

    def testPrimeNumber(self):
        self.assertEqual(True, isPrime(8))
        self.assertEqual(False, isPrime(7))
        self.assertEqual(True, isPrime(4391))

if __name__ == '__main__':
   unittest.main()