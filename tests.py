import unittest
import tp_list_tuple

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

