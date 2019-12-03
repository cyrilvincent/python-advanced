class Mesure:

    counter = 0

    def __init__(self, T, AT, VT, AM, VM):
        self.T = T
        self.AT = AT
        self.VT = VT
        self.AM = AM
        self.VM = VM
        Mesure.counter += 1

    def power(self):
        return self.AM * self.VM

    def error(self):
        return abs(self.VM - self.VT)

    def squareError(self):
        return (self.VM - self.VT)**2

    def __del__(self):
        Mesure.counter -= 1

import unittest
class MesureTest(unittest.TestCase):

    def testPower(self):
        m = Mesure(0,0,0,10.0,20.0)
        self.assertAlmostEqual(200.0, m.power(),delta=1e-4)

    def testError(self):
        m = Mesure(0, 0, 100.0, 0, 102.0)
        self.assertAlmostEqual(2.0, m.error(), delta=1e-4)

    def testEquality(self):
        m1 = Mesure(0, 0, 100.0, 0, 102.0)
        m2 = Mesure(0, 0, 100.0, 0, 102.0)
        print(m1)
        print(m2)
        self.assertNotEqual(m1, m2)

    def testStatic(self):
        m1 = Mesure(0, 0, 100.0, 0, 102.0)
        m2 = Mesure(0, 0, 100.0, 0, 102.0)
        self.assertEqual(2, Mesure.counter)
        del m1
        self.assertEqual(1, Mesure.counter)

