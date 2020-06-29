import unittest

class TP1Test(unittest.TestCase):

    def testIsEven(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(7))

    def testIsPrime(self):
        self.assertTrue(isPrime(7))
        self.assertFalse(isPrime(8))
        self.assertTrue(isPrime(2))
