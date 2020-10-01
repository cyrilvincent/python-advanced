import datetime
from typing import List

class Publisher:

    def __init__(self, name):
        self.name = name

# Créer la classe Media, Cd, Dvd
# Le panier doit accepter indifférement des medias
# Attention au prix TTC, TVA = 20%

class Book:

    tva = 0.055
    _nbBook = 0

    def __init__(self, title, price, publicationDate = datetime.datetime.now(), color = "", authors = [], nbPage = 0, publisher:Publisher = None):
        self.title = title
        self._price = price
        self.publicationDate = publicationDate
        self.color = color
        self.nbPage = nbPage
        self.publisher = publisher
        self.authors = authors
        Book._nbBook += 1

    @staticmethod
    def nbBook():
        return Book._nbBook

    @classmethod
    def nbBook2(cls):
        return cls._nbBook

    def netPrice(self):
        return self._price * (1 + Book.tva)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price <= 0")
        else:
            self._price = value

    def __del__(self):
        Book._nbBook -= 1

class Cart:

    def __init__(self):
        self.items:List[Book] = []

    @property
    def nbItem(self):
        return len(self.items)

    def add(self, item:Book):
        self.items.append(item)

    def remove(self, item:Book):
        self.items.remove(item)

    @property
    def totalNetPrice(self):
        sum = 0
        for item in self.items:
            sum += item.netPrice()
        return sum
        #return sum([item.netPrice() for item in self.items])

    def removeAll(self, item):
        for _ in range(self.items.count(item)):
            self.items.remove(item)
