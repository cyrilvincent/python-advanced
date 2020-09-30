import unittest
import demo
import math
import geometry

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
        res = filter(lambda x : x % 2 == 0, l)
        res = map(lambda x : x ** 2, res)
        res = list(res)
        self.assertListEqual([0, 4, 16], res)

    def test_evenprime(self):
        l = range(5)
        res = filter(demo.is_prime, l)
        res = filter(lambda x : x % 2 == 0, res)
        # res = list(res)
        # self.assertListEqual([2], res)
        # for i in res:
        #     print(i)

    def test_intention_list(self):
        l = range(5)
        res = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, l)))
        # <=>
        res = [x ** 2 for x in l if x % 2 == 0]
        self.assertListEqual([0, 4, 16], res)
        #Refaire l'exercice filter + map et filter + filter avec des liste en intention
        # Filtrer les nombres premiers  et passer au carré
        # Filtrer les nombres premiers et les pairs

        res = [x ** 2 for x in l if demo.is_prime(x)]
        self.assertListEqual([4,9], res)

        res = [x for x in l if demo.is_prime(x)]
        res = [x for x in res if x % 2 == 0]
        self.assertListEqual([2], res)

        res = [x for x in l if demo.is_prime(x) and x % 2 == 0]
        self.assertListEqual([2], res)

    def test_value_reference(self):
        i = 2
        j = i
        self.assertEqual(i,j)
        j += 1
        self.assertEqual(3, j)
        self.assertEqual(2, i)
        l1 = [1,2,3]
        l2 = l1
        l2.append(4)
        self.assertEqual([1,2,3,4], l2)
        self.assertEqual([1, 2, 3, 4], l1)
        l3 = [1,2,3,4]
        self.assertTrue(l2 == l3)
        self.assertFalse(l2 is l3)
        self.assertTrue(l2 is l1)

        l1 = [1,2,3]
        l2 = list(l1)
        l1.append(4)

    def test_tuple(self):
        res = demo.demo_tuple()
        self.assertEqual(1, res[0])
        self.assertEqual(99, res[1])

        (a,b) = demo.demo_tuple()
        self.assertEqual(1, a)
        self.assertEqual(99, b)

        a,b = demo.demo_tuple()
        self.assertEqual(1, a)
        self.assertEqual(99, b)

    def test_min_max_avg(self):
        l = range(10)
        min, max, avg = demo.min_max_avg(l)
        self.assertEqual(0, min)
        self.assertEqual(9, max)
        self.assertEqual(4.5, avg)

    def test_min_max_avg_dico(self):
        l = range(10)
        dico = demo.min_max_avg_dico(l)
        self.assertEqual(0, dico["min"])
        self.assertEqual(9, dico["max"])
        self.assertEqual(4.5, dico["avg"])

    def test_dico(self):
        dico = demo.dico()
        self.assertEqual("Hans Christian Andersen", dico["author"])

    def test_rectangle(self):
        r1 = geometry.Rectangle(width=3,length=2)
        self.assertEqual(3, r1.width)
        self.assertEqual(10, r1.perimeter())
        self.assertEqual(6, r1.area())
        self.assertEqual(6, geometry.Rectangle.area(r1))
        r2 = geometry.Rectangle(width=3, length=2)
        r1 = r2
        self.assertEqual(r1, r2)



if __name__ == '__main__':
    unittest.main()

