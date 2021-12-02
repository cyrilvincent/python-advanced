import math
import unittest
import mylib
import demo_yield

class MyTests(unittest.TestCase):

    def test_isprime(self):
        #AAA Act Arange Assert
        res = mylib.is_prime(7)
        self.assertTrue(res)
        res = mylib.is_prime(8)
        self.assertFalse(res)

    def test_assert(self):
        i = 1 + 1
        self.assertEqual(2, i)
        res = math.sqrt(2)
        self.assertAlmostEqual(1.414, res, delta=1e-3)

    def test_myfilter_dirty(self):
        l = [1, 2, 3, 4, 5, 6]
        res = demo_yield.myfilter_dirty(lambda x: x % 2 == 0, l)
        self.assertEqual([2, 4, 6], res)
        res = demo_yield.myfilter_dirty(lambda x: mylib.is_prime(x), l)
        self.assertEqual([2,3,5], res)

    def test_filter(self):
        l = [1, 2, 3, 4, 5, 6]
        res = demo_yield.filter(lambda x: x % 2 == 0, l)
        self.assertEqual([2, 4, 6], list(res))

    def test_map(self):
        l = [1, 2, 3, 4, 5, 6]
        res = demo_yield.map(lambda x: x + 1, l)
        self.assertEqual([2, 3, 4, 5, 6, 7], list(res))

    def test_filter_map(self):
        l = [1, 2, 3, 4, 5, 6]
        res = demo_yield.filter(lambda x: mylib.is_prime(x), l)
        res = demo_yield.map(lambda x: x * 2, res)
        self.assertEqual([4, 6, 10], list(res))

    def test_generator(self):
        l = [1, 2, 3, 4, 5, 6]
        res = (x * 2 for x in l if mylib.is_prime(x))
        self.assertEqual([4, 6, 10], list(res))

    def test_comprehension(self):
        l = [1, 2, 3, 4, 5, 6]
        res = list((x * 2 for x in l if mylib.is_prime(x)))
        # <=>
        res = [x * 2 for x in l if mylib.is_prime(x)]
        self.assertEqual([4, 6, 10], res)

    def test_error(self):
        l = [1, 2, 3, 4, 5, 6]
        res = (x * 2 for x in l if mylib.is_prime(x))
        with self.assertRaises(Exception):
            _ = len(res)

    def test_infinite(self):
        res = (x * 2 for x in demo_yield.infinite() if mylib.is_prime(x))
        for i in res:
            print(i)


