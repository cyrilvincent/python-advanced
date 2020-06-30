import datetime
from typing import *

class Publisher:

    def __init__(self, name):
        self.name = name

class Book:

    nbBook = 0
    vat = 0.055

    def __init__(self, id, title, price, author=None, nbPage=0, date=datetime.datetime.now(), publisher = Publisher(None) ):
        self.id = id
        self.title = title
        self._price = price
        self.author = author
        self.nbPage = nbPage
        self.date = date
        self.publisher = publisher
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
        return self._price * (1 + Book.vat)

    def __del__(self):
        Book.nbBook -= 1

class Cart:

    def __init__(self):
        self.items:List[Book]=[]

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    @property
    def totalNetPrice(self):
        return sum([i.netPrice for i in self.items])

    @property
    def nbItem(self):
        return len(self.items)

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

    def testPublisher(self):
        p = Publisher("O'Reilly")
        b = Book(0,None,0,publisher=p)
        self.assertEqual("O'Reilly", b.publisher.name)

    def testCart(self):
        cart = Cart() #Liste de Book
        b = Book(0,"Python",10)
        cart.add(b)
        self.assertEqual(1, cart.nbItem)
        b2 = Book(1,"Numpy",20)
        cart.add(b2)
        self.assertEqual(2, cart.nbItem)
        self.assertAlmostEqual((10.+20.)*1.055, cart.totalNetPrice, delta=1e-4)
        cart.remove(b2)
        self.assertEqual(1, cart.nbItem)

    # Gérer des Book(nbPage), Cd(nbTrack), Dvd(zone)
    # Media
    # Gérer la TVA 20%
    # Bonus : Stylo, MachineALaver => Item
    # MAJ Cart
