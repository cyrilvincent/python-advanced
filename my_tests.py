import unittest
import tp1
import geometry

class MyTests(unittest.TestCase):

    def test_first(self):
        self.assertEqual(2, 1+1)

    def test_float(self):
        self.assertAlmostEqual(1.414, 2 ** 0.5, delta=1e-3)

    def test_is_prime(self):
        self.assertTrue(tp1.is_prime(7))
        self.assertFalse(tp1.is_prime(9))

    def test_rectangle(self):
        r = geometry.Rectangle(2,3)
        self.assertEqual(6, r.area())
        self.assertEqual(10, r.perimeter())
