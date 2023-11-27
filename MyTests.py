import unittest

class MyTests(unittest.TestCase):

    def test_debile(self):
        self.assertEqual(3, 1+2)
        my_bool = 1 < 2
        self.assertTrue(my_bool)

    def test_round(self):
        a = 2 ** 0.5
        self.assertAlmostEqual(1.414, a, delta=0.001)
        b = a ** 2
        self.assertAlmostEqual(2, b, delta=0.001)


