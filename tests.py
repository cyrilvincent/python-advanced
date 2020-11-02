import unittest
import hello
import tp1
import tp2
import demotuple

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

    def test_tp_filter_map(self):
        l = range(10)
        res = list(filter(lambda x : x % 2 == 0, l))
        self.assertEqual([0,2,4,6,8], res)
        res = list(filter(tp1.is_prime, l))
        self.assertEqual([2,3,5,7], res)
        res = list(filter(lambda x: x % 2 == 0 and tp1.is_prime(x), l))
        res = filter(lambda x : x % 2 == 0, l)
        res = list(filter(tp1.is_prime, res))
        self.assertEqual([2], res)
        res = list(filter(tp1.is_prime, l))
        res = list(map(lambda x : x ** 2, res))
        self.assertEqual([4, 9, 25, 49], res)
        res = list(map(lambda x : x ** 2, filter(lambda x : tp1.is_prime(x), l)))
        self.assertEqual([4, 9, 25, 49], res)

    def test_intention_list(self):
        l = range(10)
        res = [x for x in l if x % 2 == 0]
        res = [x for x in l if tp1.is_prime(x)]
        res = [x for x in l if tp1.is_prime(x) and x % 2 == 0]
        res = [x ** 2 for x in l if tp1.is_prime(x)]
        self.assertEqual([4, 9, 25, 49], res)

    def test_tuple(self):
        l = range(11)
        min,max,avg = demotuple.min_max_avg(l)
        self.assertEqual(0, min)
        self.assertEqual(10, max)
        self.assertEqual(5, avg)

    def test_dico(self):
        l = range(11)
        dico = demotuple.min_max_avg_dico(l)
        self.assertEqual(0, dico["min"])
        self.assertEqual(10,  dico["max"])
        self.assertEqual(5,  dico["avg"])

