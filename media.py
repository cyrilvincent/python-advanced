import datetime
import unittest
import abc
import csv
import sqlite3

# Book : nbPage, Cd : NbTrack, Dvd : zone
# Media : id, title, price, author, editor, publication
# bonus : Item : id, title, price
# 15h40

class Item(metaclass=abc.ABCMeta): # Abstraite interdit de faire Item()

    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

    @property
    @abc.abstractmethod
    def netPrice(self):...

class Media(Item, metaclass=abc.ABCMeta):

    def __init__(self, id, title, price, author, editor = None, publicationDate = datetime.datetime.now(), category=None):
        Item.__init__(self, id,title,price)
        self.author = author
        self.editor = editor
        self.publicationDate = publicationDate
        self.category = category

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

class Book(Media):
    nbBook = 0

    def __init__(self, isbn, title, price, author, editor = None, publicationDate = datetime.datetime.now(), category=None, nbPage = 0):
        super().__init__(isbn,title,price,author,editor,publicationDate,category)
        self.nbPage = nbPage
        Book.nbBook += 1

    @property
    def netPrice(self):
        return self.price * 0.95 * 1.055 + 0.01

    def __del__(self):
        Book.nbBook -= 1

class Cd(Media):

    def __init__(self, id, title, price, author, editor = None, publicationDate = datetime.datetime.now(), category=None, nbTrack = 0):
        super().__init__(id,title,price,author,editor,publicationDate,category)
        self.nbTrack = nbTrack

    def netPrice(self):
        return self.price * 1.2


class Cart:

    def __init__(self):
        self.items = []

    def add(self, item: Media):
        self.items.append(item)

    def remove(self, item:Media):
        self.items.remove(item)

    @property
    def nbItems(self):
        return len(self.items)

    @property
    def netPrice(self):
        # total = 0
        # for media in self.items:
        #     total += media.netPrice
        # return total
        return sum([m.netPrice for m in self.items])

class MediaRepository(metaclass=abc.ABCMeta):

    def __init__(self, path):
        self.path = path
        self.items = [] # List de media

    @abc.abstractmethod
    def load(self):...

    def getByPrice(self, price):
        return [m for m in self.items if m.price <= price]

    def getByTitle(self, title):
        return [m for m in self.items if title.upper() in m.title.upper()]

class CsvRepository(MediaRepository):

    def load(self):
        with open(self.path) as f:
            reader = csv.DictReader(f)
            self.items = [Book(row["id"], row["title"], float(row["price"]), "Cyril") for row in reader]

class SqlRepository(MediaRepository):

    def load(self):
        with sqlite3.connect(self.path) as connect:
            cursor = connect.execute("select id,title,price from book")
            self.items = [Book(row[0], row[1], row[2], "Cyril") for row in cursor]

class MediaTest(unittest.TestCase):

    def testBook(self):
        b1 = Book("123","Python",10,"Cyril")
        netPrice = b1.netPrice
        self.assertAlmostEqual(10.0324, netPrice,delta=1e-3)
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

    def testPolymorphism(self):
        #item = Item(0,"",0) interdit
        cd = Cd("123", "Johnny", 10, "Cyril")
        print(cd.netPrice)

    def testCsvRepository(self):
        repo = CsvRepository("data/media/books.csv")
        repo.load()
        self.assertTrue(len(repo.items) > 0)
        print(repo.items)
        l = repo.getByPrice(11)
        self.assertEqual(2, len(l))
        l = repo.getByTitle("python")
        self.assertEqual(2, len(l))

    def testSqlRepository(self):
        repo=SqlRepository("data/media/books.db3")
        repo.load()
        self.assertTrue(len(repo.items) > 0)
        print(repo.items)
        l = repo.getByPrice(11)
        self.assertEqual(2, len(l))
        l = repo.getByTitle("python")
        self.assertEqual(1, len(l))

    def testDict(self):
        cd = Cd("123", "Johnny", 10, "Cyril")
        dico = cd.__dict__
        self.assertEqual("123", dico["id"])
        dico["titi"]="toto"
        cd.__dict__ = dico
        self.assertEqual("toto", cd.titi)
        import json
        import bson
        with open("data/media/cd.json","w") as f:
            json.dump(dico, f,default=str)

    def testEquality(self):
        cd1 = Cd("123", "Johnny", 10, "Cyril")
        cd2 = Cd("123", "Johnny", 10, "Cyril")
        self.assertEqual(cd1,cd2)
