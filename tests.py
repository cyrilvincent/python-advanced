import unittest
import hello
import tp1

class MyTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(2,1+1)

    def test_add(self):
        res = hello.add(2,3)
        self.assertEqual(5, res)

    def test_iseven(self):
        self.assertTrue(tp1.is_even(8))
        self.assertFalse(tp1.is_even(9))
        # 3 % 2 = 1

    def test_isprime(self):
        self.assertTrue(tp1.is_prime(7))
        self.assertFalse(tp1.is_prime(8))
        self.assertTrue(tp1.is_prime(2731))
        # Un nombre premier est un nombre qui possède exactement 2 diviseurs : 1 et lui même
        # Un nombre est premier sauf s'il possède un diviseur entre 2 et n-1