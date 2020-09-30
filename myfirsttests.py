import unittest
import demo
import math

class MyTests(unittest.TestCase):

    def test_1(self):
        i = 1
        i += 1
        self.assertEqual(2,i)

    def test_prime_number(self):
        self.assertTrue(demo.is_prime(x=7))
        self.assertFalse(demo.is_prime(8))
        self.assertFalse(demo.is_prime(1))

    def test_var_function(self):
        fn = demo.is_prime
        self.assertTrue(fn(7))

    def test_lambda(self):
        # f(x) = x + 1 <=>
        f = lambda x : x + 1
        self.assertEqual(2,f(1))

    def test_filter_even(self):
        l = [0,1,2,3]
        res = demo.filter_even(l)
        self.assertListEqual([0,2], res)

    def test_myfilter(self):
        l = [0,1,2,3,4,5,6,7]
        res = demo.myfilter(demo.is_prime, l)
        self.assertListEqual([2,3,5,7], res)

    def test_filter(self):
        l = [0,1,2,3,4,5,6,7]
        res = filter(demo.is_prime, l)
        res = list(res)
        print(res)
        self.assertListEqual([2,3,5,7], res)

    def test_map(self):
        l = [0, 1, 2, 3, 4]
        res = demo.mymap(demo.double, l)
        self.assertListEqual([0,2,4,6,8], res)
        res = map(demo.double, l)
        res = list(res)
        self.assertListEqual([0,2,4,6,8], res)
        res = map(lambda x : x + 1, l)
        res = list(res)
        self.assertListEqual([1,2,3,4,5], res)

    def test_tp1(self):
        l = range(5)
        # Filtrer les nombres pairs
        # Monter au carré les nombres pairs
        self.assertListEqual([0, 4, 16], res)
        # Obtenir la racine carrée des nombres premiers de l
        self.assertAlmostEqual(2, math.sqrt(2) ** 2,delta=1e-5)




if __name__ == '__main__':
    unittest.main()

