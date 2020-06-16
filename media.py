import datetime
import unittest

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


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item: Book):
        self.items.append(item)

    def remove(self, item:Book):
        self.items.remove(item)

    @property
    def nbItems(self):
        return len(self.items)

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

    def testCart(self):
        cart = Cart()
        self.assertEqual(0, cart.nbItems)
        b1 = Book("123", "Python", 10, "Cyril")
        cart.add(b1)
        self.assertEqual(1, cart.nbItems)
        cart.remove(b1)
        self.assertEqual(0, cart.nbItems)