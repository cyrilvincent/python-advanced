import datetime
import unittest

class Book:

    def __init__(self, isbn, title, price, author, editor = None, publicationDate = datetime.datetime.now(), category=None):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.author = author
        self.editor = editor
        self.publicationDate = publicationDate
        self.category = category

    def getNetPrice(self):
        return self.price * 1.055
    # A passer en propriété lecture seule

class MediaTest(unittest.TestCase):

    def testBook(self):
        b1 = Book("123","Python",10,"Cyril")
        netPrice = b1.getNetPrice()
        self.assertAlmostEqual(10.55, netPrice,delta=1e-3)
        b2 = Book("123", "Python", 10, "Cyril", publicationDate=datetime.datetime(2020,6,16))
