l = [1,5,99,-8,2,7,45]

def min_max_avg(l):
    min = l[0]
    max = l[0]
    sum = l[0]
    nb = 1
    for val in l[1:]:
        if val < min:
            min = val
        elif val > max:
            max = val
        sum += val
        nb += 1
    return min, max, sum / nb

import unittest

class TP3Test(unittest.TestCase):

    def testtp(self):
        min, max, avg = min_max_avg(l)
        self.assertEqual(min, -8)
        self.assertEqual(max, 99)
        self.assertAlmostEqual(avg, 21.571, delta = 1e-3)