import datetime

class Book:

    nbBook = 0

    def __init__(self, id, title, price, author=None, nbPage=0, date=datetime.datetime.now()):
        self.id = id
        self.title = title
        self._price = price
        self.author = author
        self.nbPage = nbPage
        self.date = date
        Book.nbBook += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Negative price")
        else:
            self._price = value

    @property
    def netPrice(self):
        return self._price * 1.055

    def __del__(self):
        Book.nbBook -= 1

import unittest
class MediaTest(unittest.TestCase):

    def testBook(self):
        b = Book(0,None,10)
        self.assertAlmostEqual(10 * 1.055, b.netPrice, 1e-4)

    def testNbBook(self):
        b = Book(0,None,0)
        self.assertEqual(1, Book.nbBook)
        del(b)
        self.assertEqual(0, Book.nbBook)

    def testNegativePrice(self):
        b = Book(0,None,0)
        with self.assertRaises(ValueError):
            b.price = -10
