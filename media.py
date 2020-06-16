import datetime
import unittest

class Cart:
    pass
    # Cart = Liste de Book
    # Au départ elle est vide
    # Ajouter
    # Remove

class Book:

    nbBook = 0

    def __init__(self, isbn, title, price, author, editor = None, publicationDate = datetime.datetime.now(), category=None):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.author = author
        self.editor = editor
        self.publicationDate = publicationDate
        self.category = category
        Book.nbBook += 1

    def __del__(self):
        Book.nbBook -= 1

    @property
    def netPrice(self):
        return self.price * 1.055


class MediaTest(unittest.TestCase):

    def testBook(self):
        b1 = Book("123","Python",10,"Cyril")
        netPrice = b1.netPrice
        self.assertAlmostEqual(10.55, netPrice,delta=1e-3)
        b2 = Book("123", "Python", 10, "Cyril", publicationDate=datetime.datetime(2020,6,16))

    def testNbBook(self):
        self.assertEqual(0, Book.nbBook)
        b1 = Book("123", "Python", 10, "Cyril")
        self.assertEqual(1, Book.nbBook)
        b2 = Book("123", "Python", 10, "Cyril")
        self.assertEqual(2, Book.nbBook)
        del(b2)
        self.assertEqual(1, Book.nbBook)