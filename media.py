import datetime
import unittest
import abc

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

    @abc.abstractmethod
    def getByPrice(self, price):... #Retrouver tous les medias price <= paramètre

    @abc.abstractmethod
    def getByTitle(self, title):... #Retrouver tous les medias contenant le title BONUS

class CsvRepository(MediaRepository):
    pass

class SqlRepository(MediaRepository):
    pass

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

    def testPolymorphism(self):
        #item = Item(0,"",0) interdit
        cd = Cd("123", "Johnny", 10, "Cyril")
        print(cd.netPrice)

