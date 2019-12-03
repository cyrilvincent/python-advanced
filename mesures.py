import abc
class MesuresRepository(metaclass=abc.ABCMeta):

    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def load(self):...

    @abc.abstractmethod
    def powers(self):...

    @abc.abstractmethod
    def errors(self): ...

class MesuresCSV(MesuresRepository):

    def __init__(self, path):
        super().__init__(path)

    



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

    def __repr__(self):
        return f"Mesure T: {self.T} AM: {self.AM} VM: {self.VM}"

class MesureWithT(Mesure):

    def __init__(self, T, AT, VT, AM, VM, Temp):
        super().__init__(T, AT,VT,AM,VM)
        self.Temp = Temp

    def __repr__(self):
        return super().__repr__() + f"Temp: {self.Temp}"


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

    def testMesuresCSV(self):
        mesuresCSV = MesuresCSV("mesures/mesures.csv")
        mesuresCSV.load()

