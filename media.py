import datetime
import abc
from typing import List

class Publisher:

    def __init__(self, name):
        self.name = name

#Rendre Media abstrait + netPrice abstrait
#Book : price * (1 + TVA) * 0.95 + 0.01
#Vérifier que le prix TTC du panier marche toujours

class Media(metaclass=abc.ABCMeta):
    tva = 0.2

    def __init__(self, title, price, publicationDate = datetime.datetime.now(), color = "", authors=None, publisher:Publisher = None):
        if authors is None:
            authors = []
        self.title = title
        self._price = price
        self.publicationDate = publicationDate
        self.color = color
        self.publisher = publisher
        self.authors = authors

    @abc.abstractmethod
    def netPrice(self):...

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price <= 0")
        else:
            self._price = value

    def __eq__(self, other):
        return self.title == other.title \
               and self.price == other.price

    def __ne__(self, other):
        return not self.__eq__(other)

class Book(Media):

    tva = 0.055
    _nbBook = 0

    def __init__(self, title, price, publicationDate = datetime.datetime.now(), color = "", authors=None, publisher:Publisher = None, nbPage = 0):
        super().__init__(title,price,publicationDate,color,authors,publisher)
        self.nbPage = nbPage
        self._isbn = None
        Book._nbBook += 1

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        pass

    def netPrice(self):
        return self._price * (1 + Book.tva) * 0.95 + 0.01

    @staticmethod
    def nbBook():
        return Book._nbBook

    @classmethod
    def nbBook2(cls):
        return cls._nbBook

    def __del__(self):
        Book._nbBook -= 1

class Cd(Media):

    def __init__(self, title, price, publicationDate=datetime.datetime.now(), color="", authors=None,
                 publisher: Publisher = None, nbTrack=0):
        Media.__init__(self,title,price,publicationDate,color,authors,publisher)
        self.nbTrack = nbTrack

    def netPrice(self):
        return self._price * (1 + Media.tva)

class Cart:

    def __init__(self):
        self.items:List[Media] = []

    @property
    def nbItem(self):
        return len(self.items)

    def add(self, item:Media):
        self.items.append(item)

    def remove(self, item:Media):
        self.items.remove(item)

    @property
    def totalNetPrice(self):
        # sum = 0
        # for item in self.items:
        #     sum += item.netPrice()
        # return sum
        return sum([item.netPrice() for item in self.items])

    def removeAll(self, item):
        for _ in range(self.items.count(item)):
            self.items.remove(item)
