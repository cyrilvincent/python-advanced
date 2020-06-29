import unittest
import math

def add(i:float,j:float)->float:
    return i+j

def isEven(x:int)->bool:
    return x % 2 == 0

class DemoTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(2,1+1)

    def testAdd(self):
        self.assertEqual(2, add(1,j=1))
        self.assertTrue(1+1 == 2)
        toto = add
        self.assertEqual(2, toto(1, j=1))

    def testSin(self):
        self.assertAlmostEqual(0, math.sin(math.pi),delta=1e-4)

    def testIsEven(self):
        self.assertTrue(isEven(8))
        self.assertFalse(isEven(7))



if __name__ == '__main__':
    unittest.main()
