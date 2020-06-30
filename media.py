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

    def __del__(self):
        pass

import unittest
class MediaTest(unittest.TestCase):

    def testBook(self):
        b = Book(0,None,10)
        self.assertAlmostEqual(10 * 1.055, b.getNetPrice(), 1e-4)

    # Passer le self.price en privé + getter + setter
    # Dans le setter interdire les price < 0
    # Passer le netPrice en @property
    # Compter automatiquement les livres instanciés
