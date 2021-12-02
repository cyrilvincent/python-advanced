import math
import unittest
import mylib

class MyTests(unittest.TestCase):

    def test_isprime(self):
        #AAA Act Arange Assert
        res = mylib.is_prime(7)
        self.assertTrue(res)
        res = mylib.is_prime(8)
        self.assertFalse(res)

    def test_assert(self):
        i = 1 + 1
        self.assertEqual(2, i)
        res = math.sqrt(2)
        self.assertAlmostEqual(1.414, res, delta=1e-3)