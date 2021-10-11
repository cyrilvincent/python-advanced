import unittest
# from typing import List
import mylib


class MyClass(unittest.TestCase):

    def test1(self):
        self.assertEqual(2, 1+1)

    def test_iseven(self):
        res = mylib.is_even(8)
        self.assertTrue(res)

    def test_isprime(self):
        self.assertTrue(mylib.is_prime(7))
        self.assertFalse(mylib.is_prime(8))
