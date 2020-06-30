import datetime

class Book:

    def __init__(self, id, title, price, author=None, nbPage=0, date=datetime.datetime.now()):
        self.id = id
        self.title = title
        self.price = price
        self.author = author
        self.nbPage = nbPage
        self.date = date

    def getNetPrice(self):
        return self.price * 1.055

import unittest
class MediaTest(unittest.TestCase):

    def testBook(self):
        b = Book(0,None,10)
        self.assertAlmostEqual(10 * 1.055, b.getNetPrice(), 1e-4)
