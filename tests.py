import unittest
import hello
import tp1

class MyTest(unittest.TestCase):


    def test1(self):
        self.assertEqual(2, 1+1)

    def test_add(self):
        res = hello.add(2, 3)
        self.assertEqual(5, res)

    def test_iseven(self):
        self.assertTrue(tp1.is_even(8))
        self.assertFalse(tp1.is_even(9))
        # 3 % 2 = 1

    def test_isprime(self):
        self.assertTrue(tp1.is_prime(7))
        self.assertFalse(tp1.is_prime(8))
        self.assertTrue(tp1.is_prime(2731))
        self.assertTrue(tp1.is_prime("toto"))
        # Un nombre premier est un nombre qui possède exactement 2 diviseurs : 1 et lui même
        # Un nombre est premier sauf s'il possède un diviseur entre 2 et n-1

    def test_complex_function(self):
        tp1.complex_function(1,2,3,4,5,6,toto=7,titi=8)
        print(type(tp1.complex_function))
        f = tp1.complex_function
        f(3,4)

    def test_list(self):
        l = [0,1,3,5,9,-1,10,3,8,3,99]
        res = tp2.remove_all(l, 3)
        self.assertEqual([0,1,5,9,-1,10,8,99])
        res = tp2.filter_even(l)
        self.assertEqual([0,10,8])
        res = tp2.filter_prime(l)
        self.assertEqual([3,5,3,3])
        # Bonus : Essayer d'optimiser les 2 fonctions de filtre