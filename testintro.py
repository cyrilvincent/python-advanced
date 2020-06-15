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
        self.assertEqual(True, intro.isPrime(x=4391))

    def testVerification(self):
        self.assertEqual(True, intro.verify(2, intro.isEven))
        self.assertEqual(True, intro.verify(7, intro.isPrime))

    def testFilterByFn(self):
        l = [0,1,2,3,4,5,6,7,8,9]
        self.assertListEqual([0,2,4,6,8], intro.filterByFn(intro.isEven, l))
        self.assertListEqual([2,3,5,7], intro.filterByFn(intro.isPrime, l))
        self.assertListEqual([6,7,8,9], intro.filterByFn(intro.isGreaterThan, l))

if __name__ == '__main__':
   unittest.main()