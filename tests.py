import unittest
import tp_list_tuple
import geometry
import bank

class Tests(unittest.TestCase):

    def test_debile(self):
        a = 1
        a = a + 1
        self.assertEqual(2, a, "a doit être égal à 2")
        self.assertAlmostEqual(1.414, 2 ** 0.5, delta=0.001)

    def test_min_max_avg(self):
        l = [1,2,5,99,-1,4,88,66,0,88]
        min, max, avg = tp_list_tuple.min_max_avg(l)
        self.assertEqual(-1, min)

    def test_rectangle(self):
        r1 = geometry.Rectangle(3, 2)
        self.assertEqual(3, r1.length)
        self.assertEqual(6, r1.area())
        self.assertEqual(10, r1.perimeter())
        
    def test_bank_credit(self):
        a = bank.Account("001", "Cyril", "CNRS")
        self.assertEqual(0, a.balance)
        a.credit(50)
        self.assertEqual(50, a.balance)

    def test_bank_debit(self):
        a = bank.Account("001", "Cyril", "CNRS")
        a.credit(50)
        a.debit(20)
        self.assertEqual(30, a.balance)

    def test_bank_debit_robust(self):
        a = bank.Account("001", "Cyril", "CNRS")
        a.credit(50)
        with self.assertRaises(ValueError):
            a.debit(100)

    def test_bank(self):
        b = bank.Bank("123", "MyBank", "01234567890")
        self.assertIsNotNone(b)

    
