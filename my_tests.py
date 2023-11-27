import unittest
import rappels

class MyTests(unittest.TestCase):

    def test_debile(self):
        self.assertEqual(3, 1+2)
        my_bool = 1 < 2
        self.assertTrue(my_bool)

    def test_round(self):
        a = 2 ** 0.5
        self.assertAlmostEqual(1.414, a, delta=0.001)
        b = a ** 2
        self.assertAlmostEqual(2, b, delta=0.001)

    def test_is_prime(self):
        self.assertTrue(rappels.is_prime(7))
        self.assertFalse(rappels.is_prime(8))

    def test_filter_prime(self):
        l = [1,3,8,99,100,10,13,17,2,18]
        res = rappels.filter_prime(l)
        self.assertEqual([3,13,17,2], res)


