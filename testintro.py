import unittest
import math
import intro

class MyTests(unittest.TestCase):

    def testFirst(self):
        self.assertEqual(2, 1+1)

    def testIsEven(self):
        res = intro.isEven(8)
        self.assertEqual(True, res)
        self.assertEqual(False, intro.isEven(7))

    def testAlmostEqual(self):
        self.assertAlmostEqual(3.14, math.pi, delta=1e-2)
        self.assertAlmostEqual(2, math.sqrt(2) ** 2, delta=1e-5)

    def testPrimeNumber(self):
        self.assertEqual(False, intro.isPrime(8))
        self.assertEqual(True, intro.isPrime(7))
        self.assertEqual(True, intro.isPrime(4391))

if __name__ == '__main__':
   unittest.main()