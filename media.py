#1 Créer le module media.py
#2 Créer la class Book
#3 getNetPrice() : price * 1.055
#4 Tester

import unittest
import abc

class Media(metaclass=abc.ABCMeta):

    def __init__(self, id:int, title:str, price:float, author=None, publisher=None):
        self.id = id
        self.title = title
        self.price = price
        self.author = author
        self.publisher = publisher

    @abc.abstractmethod
    def getNetPrice(self):...

    def __repr__(self):
        return f"{type(self)} {self.id} {self.title}"

    def __lt__(self, other):
        return self.price - other.price

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id # != not(==)

class Book(Media):

    nbBook = 0

    def __init__(self, id:int, title:str, price:float, author=None, publisher=None, nbPage = 0):
        super().__init__(id,title,price,author,publisher)
        self.nbPage = nbPage
        Book.nbBook += 1

    def getNetPrice(self):
        return self.price * 1.055 * 0.95 + 0.01

    def __del__(self):
        Book.nbBook -= 1

class Cd(Media):

    def __init__(self, id:int, title:str, price:float, author=None, publisher=None, nbTrack = 0):
        super().__init__(id,title,price,author,publisher)
        self.nbTrack = nbTrack

    def getNetPrice(self):
        return self.price * 1.2 * 0.8

class Cart:

    def __init__(self):
        self.medias = []

    def add(self, book):
        self.medias.append(book)

    def remove(self, book):
        self.medias.remove(book)

    def clear(self):
        self.medias.clear()

    def getTotalNetPrice(self):
        return sum([b.getNetPrice() for b in self.medias])

class MediaTest(unittest.TestCase):

    def testBook(self):
        b = Book(0,"Python",10.0,nbPage=10)
        self.assertAlmostEqual(10.03, b.getNetPrice(), delta = 1e-2)

    def testCountBook(self):
        b1 = Book(0,"",0)
        b2 = Book(0,"",0)
        self.assertEqual(2,Book.nbBook)
        b1 = None
        self.assertEqual(1, Book.nbBook)
        del b2
        self.assertEqual(0, Book.nbBook)

    def testCart(self):
        c = Cart()
        self.assertEqual(0, len(c.medias))
        b= Book(0,"",10)
        c.add(b)
        self.assertEqual(1, len(c.medias))
        c.add(Cd(1,"",20))
        self.assertAlmostEqual(29.23, c.getTotalNetPrice(), delta = 1e-2) # liste en intention + sum()



