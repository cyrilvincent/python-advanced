import unittest
import math

def add(i,j):
    return i+j

def isEven(x):
    return x % 2 == 0

class DemoTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(2,1+1)

    def testAdd(self):
        self.assertEqual(2, add(1,1))
        self.assertTrue(1+1 == 2)

    def testSin(self):
        self.assertAlmostEqual(0, math.sin(math.pi),delta=1e-4)

    def testIsEven(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(9))



if __name__ == '__main__':
    unittest.main()
