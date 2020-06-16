import datetime
import unittest

class Book:

    # Gérer nbBook

    def __del__(self):
        pass
        # var = var1
        # var = None
        # del(var)
        # Sort d'une fonction pour les variables locales
        # Garbage Collector

    def __init__(self, isbn, title, price, author, editor = None, publicationDate = datetime.datetime.now(), category=None):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.author = author
        self.editor = editor
        self.publicationDate = publicationDate
        self.category = category

    @property
    def netPrice(self):
        return self.price * 1.055


class MediaTest(unittest.TestCase):

    def testBook(self):
        b1 = Book("123","Python",10,"Cyril")
        netPrice = b1.netPrice
        self.assertAlmostEqual(10.55, netPrice,delta=1e-3)
        b2 = Book("123", "Python", 10, "Cyril", publicationDate=datetime.datetime(2020,6,16))
