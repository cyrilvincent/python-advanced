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

    def test_filter_generic(self):
        l = [1, 2, 8, 7, 9, 12, 13, 99, 51, 11]
        res = rappels.filter_generic(rappels.is_prime, l)
        self.assertEqual([2, 7, 13, 11], res)


    def test_intention(self):
        l = [1,2,3,4,5,6,7,8,9]
        res = [x ** 2 for x in l if rappels.is_prime(x)]
        self.assertEqual([4,9,25,49], res)


