import unittest
import hello
import tp1
import tp2
import math

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
        # Un nombre premier est un nombre qui possède exactement 2 diviseurs : 1 et lui même
        # Un nombre est premier sauf s'il possède un diviseur entre 2 et n-1

    def test_complex_function(self):
        tp1.complex_function(1,2,3,4,5,6,toto=7,titi=8)
        print(type(tp1.complex_function))
        f = tp1.complex_function
        f(3,4)

    def test_list(self):
        l = [0,1,3,5,9,-1,10,3,8,3,99]
        res = tp2.remove_all(list(l), 3)
        self.assertEqual(res,[0,1,5,9,-1,10,8,99])
        res = tp2.filter_even(l)
        self.assertEqual(res,[0,10,8])
        res = tp2.filter_prime(l)
        self.assertEqual(res,[3,5,3,3])
        # Bonus : Essayer d'optimiser les 2 fonctions de filtre
        # Reprise 13h

    def test_filter(self):
        l = [0, 1, 3, 5, 9, -1, 10, 3, 8, 3, 99]
        res = tp2.filter(tp1.is_even, l)
        self.assertEqual(res,[0,10,8])
        l = [0, 1, 3, 5, 9, -1, 10, 3, 8, 3, 99]
        res = tp2.filter(tp1.is_prime, l)
        self.assertEqual(res,[3,5,3,3])
        l = [0, 1, 3, 5, 9, -1, 10, 3, 8, 3, 99]
        res = tp2.filter(lambda x : x % 2 == 0, l) # lambda x : x +1 : f(x) = x + 1
        print(res)
        res = list(filter(lambda x: x % 2 == 0, l))
        print(res)

    def test_map(self):
        l = [0, 1, 3, 5, 9, -1, 10, 3, 8, 3, 99]
        res = list(map(lambda x : x + 1, l))
        print(res)

    def test_reference(self):
        a = 1
        b = a
        a += 1
        self.assertEqual(1, b)
        self.assertEqual(2, a)
        l1 = [1,2,3,4]
        l2 = l1
        l1.append(5)
        self.assertEqual([1,2,3,4,5],l2)
        l3 = [1,2,3,4]
        l4 = [1,2,3,4]
        self.assertEqual(l3,l4)
        self.assertFalse(l3 is l4)
        self.assertTrue(l1 is l2)
        l1 = [1,2,3,4]
        l2 = list(l1)
        self.assertFalse(l1 is l2)
        l1.append(5)
        self.assertFalse(l1 == l2)
        print(l1,l2)

