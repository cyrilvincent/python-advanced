l = [1,5,99,-8,2,7,45]

import unittest

class TP3Test(unittest.TestCase):

    def testtp(self):
        min, max, avg = min_max_avg(l)
        self.assertEqual(min, -8)
        self.assertEqual(max, 99)
        self.assertEqual(avg, 50.0)