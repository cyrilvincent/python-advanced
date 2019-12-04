import abc
import csv

class MesuresRepository(metaclass=abc.ABCMeta):

    def __init__(self, path):
        self.path = path
        self.mesures = []

    @abc.abstractmethod
    def _load(self):...

    def powers(self):
        self._load()
        return (m.power() for m in self.mesures)

    def errors(self, delta = 1):
        self._load()
        return (m for m in self.mesures if m.error() > delta)

class MesuresCSV(MesuresRepository):

    def __init__(self, path):
        super().__init__(path)
        self.file = open(path)

    def _load(self):
        reader = csv.DictReader(self.file)
        self.mesures = (Mesure(float(row["T"]),
                               float(row["AT"]),
                               float(row["VT"]),
                               float(row["AM"]),
                               float(row["VM"])) for row in reader)

    def __del__(self):
        self.file.close()

import sqlite3
class MesuresSQL(MesuresRepository):
    """
    Select * from mesure
Select vm, vt from mesure
Select * from mesure where vm > 0
Select vm, vt from mesure where vm > 0
    """

    def __init__(self, path):
        super().__init__(path)
        self.db = sqlite3.connect(path)

    def _load(self):
        c = self.db.cursor()
        c.execute("select * from mesure")
        self.mesures = (Mesure(float(row[0]),
                               float(row[1]),
                               float(row[2]),
                               float(row[3]),
                               float(row[4])) for row in c)

    def __del__(self):
        self.db.close()

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

    def __eq__(self, other):
        return self.T == other.T and \
               self.AT == other.AT and \
               self.AM == other.AM and \
               self.VT == other.VT and \
               self.VM == other.VM

    def __ne__(self, other):
        return not(self.__eq__(other))

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
        self.assertEqual(m1, m2)

    def testStatic(self):
        m1 = Mesure(0, 0, 100.0, 0, 102.0)
        m2 = Mesure(0, 0, 100.0, 0, 102.0)
        self.assertEqual(2, Mesure.counter)
        del m1
        self.assertEqual(1, Mesure.counter)

    def testMesuresCSV(self):
        mesuresCSV = MesuresCSV("mesures/mesures.csv")
        mesuresCSV._load()

