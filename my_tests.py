import unittest
import math
import rappels

class MyTests(unittest.TestCase):

    def test_first(self):
        self.assertEqual(2, 1+1)
        self.assertTrue(1 + 1 == 2)
        self.assertAlmostEqual(1.414, math.sqrt(2), delta=0.001)

    def test_is_prime(self):
        res = rappels.is_prime(7)
        self.assertTrue(res)
        self.assertFalse(rappels.is_prime(8))

