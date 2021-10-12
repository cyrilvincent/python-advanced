import unittest
# from typing import List
import mylib
import config
import pandas
import geometry
import media
import pickle
import jsonpickle


class MyClass(unittest.TestCase):

    def test1(self):
        self.assertEqual(2, 1+1)
        pandas.read_csv()

    def test_iseven(self):
        res = mylib.is_even(8)
        self.assertTrue(res)

    def test_isprime(self):
        self.assertTrue(mylib.is_prime(7))
        self.assertFalse(mylib.is_prime(8))

    def test_sum(self):
        mylib.sum1([1,2,3])
        mylib.sum2(1,2,3)
        x = 1
        print(f"totototto {x:.1f} ")

    def test_rectangle(self):
        r1 = geometry.Rectangle(3.0,2.0)
        self.assertEqual(10, r1.perimeter())
        self.assertAlmostEqual(10,r1.perimeter(),delta=1e-2)
        self.assertAlmostEqual(6, r1.area, delta=1e-2)
        # geometry.Rectangle.perimeter(r1)
        self.assertEqual(3, r1.length)
        print(r1.coord)
        del(r1)

    def test_media(self):
        cart = media.Cart()
        b1 = media.Book(1, "Python pur les nuls", 10.0)
        cd1 = media.Cd(2, "Allumer le feu", 20.0)
        cart.add(b1)
        cart.add(cd1)
        self.assertAlmostEqual(33.99, cart.total_net_price, delta=1e-2)
        with open("data/cart.pickle", "wb") as f:
            pickle.dump(cart, f)
        with open("data/cart.json", "w") as f:
            f.write(jsonpickle.encode(cart, unpicklable=False, indent=4))
        with open("data/cart.pickle", "rb") as f:
            cart = pickle.load(f)
            self.assertIsNotNone(cart)

    def test_isbn(self):
        b1 = media.Book(1, "Python pur les nuls", 10.0)
        b1.isbn = "123-1-1234-1234-1"
        with self.assertRaises(ValueError):
            b1.isbn = "123-1-1234-1234"



    def test_polygon(self):
        # p1 = geometry.Polygon()
        t1 = geometry.Triangle()



