import unittest
from media import Book, Dvd, CartService


class MyTests(unittest.TestCase):

    def test_cart(self):
        b1 = Book(1, "Python", 10, 99)
        d1 = Dvd(2, "Scarface", 20, 2)
        service = CartService()
        service.add(b1)
        service.add(d1)
        self.assertAlmostEqual(33.9, service.get_total_net_price(), delta=0.1)
        service2 = CartService()
        self.assertEqual(2, CartService.nb_cart)
        del service2
        self.assertEqual(1, CartService.nb_cart)
