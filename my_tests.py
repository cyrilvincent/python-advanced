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
        pass

    def test_intention(self):
        l = [1,2,3,4,5,6,7,8,9]
        res = [] #todo intention : filtrer les nombre premier puis renvoie au carré
        self.assertEqual([4,9,25,49], res)


