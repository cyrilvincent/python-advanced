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
        p1 = geometry.Point(-1, 1)
        r1 = geometry.Rectangle(3, 2, origin=p1)
        self.assertEqual(3, r1.length)
        self.assertEqual(6, r1.area())
        self.assertEqual(10, r1.perimeter())
        self.assertEqual(-1, r1.origin.x)
        r1.origin.relative(2, 2)
        self.assertEqual(1, r1.origin.x)
        
    def test_bank_credit(self):
        b = bank.Bank("000", "CNRS", "06")
        a = bank.Account("001", "Cyril", b)
        self.assertEqual(0, a.balance)
        a.credit(50)
        self.assertEqual(50, a.balance)

    def test_bank_debit(self):
        b = bank.Bank("000", "CNRS", "06")
        a = bank.Account("001", "Cyril", b)
        a.credit(50)
        a.debit(20)
        self.assertEqual(30, a.balance)

    def test_bank_debit_robust(self):
        b = bank.Bank("000", "CNRS", "06")
        a = bank.Account("001", "Cyril", b)
        a.credit(50)
        with self.assertRaises(ValueError):
            a.debit(100)

    def test_bank(self):
        b = bank.Bank("123", "MyBank", "01234567890")
        self.assertIsNotNone(b)

    def test_static(self):
        b = bank.Bank("000", "CNRS", "06")
        a = bank.Account("001", "Cyril", b)
        self.assertEqual(1, a.nb)
        a2 = bank.Account("001", "Cyril", b)
        self.assertEqual(2, a.nb)
        del(a2)
        self.assertEqual(1, a.nb)

    def test_transactions(self):
        b = bank.Bank("000", "CNRS", "06")
        a = bank.Account("001", "Cyril", b)
        a.credit(50)
        a.credit(50)
        a.debit(50)
        self.assertEqual(3, len(a.transactions))
        self.assertEqual(50, a.transactions[0].amount)
        self.assertEqual(-50, a.transactions[-1].amount)

    def test_square(self):
        p1 = geometry.Point(-1, 1)
        s = geometry.Square(3, p1)
        self.assertEqual(9, s.area())
        self.assertEqual(12, s.perimeter())

    def test_interest(self):
        b = bank.Bank("000", "CNRS", "06")
        a = bank.AccountWithInterest("001", "Cyril", b, 0.01)
        a.credit(100)
        self.assertAlmostEqual(1, a.compute_interest(), delta=0.01)

    def test_triangle_rectangle(self):
        p1 = geometry.Point(-1, 1)
        t = geometry.TriangleRectangle(3,4,p1)
        self.assertAlmostEqual(5, t.hypothenuse(), delta=0.001)

    def test_polymorphism(self):
        l: list[geometry.Rectangle] = []
        p1 = geometry.Point(-1, 1)
        r1 = geometry.Rectangle(3, 2, origin=p1)
        l.append(r1)
        s = geometry.Square(3, p1)
        l.append(s)
        t = geometry.TriangleRectangle(3,4,p1)
        l.append(t)
        print(l)
        areas = sum([r.area() for r in l])

    def test_portefeuille(self):
        b = bank.Bank("000", "CNRS", "06")
        a1 = bank.Account("001", "Cyril", b)
        a1.credit(100)
        a2 = bank.AccountWithInterest("001", "Cyril", b, 0.01)
        a2.credit(200)
        p = bank.Portefeuille([a1, a2])
        # p = bank.Portefeuille([])
        # p.accounts.append(a1)
        # p.accounts.append(a2)
        self.assertEqual(300, p.global_balance())

    
