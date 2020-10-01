import datetime

class Book:

    tva = 0.055
    _nbBook = 0

    def __init__(self, title, price, publicationDate = datetime.datetime.now(), color = "", authors = [], nbPage = 0):
        self.title = title
        self._price = price
        self.publicationDate = publicationDate
        self.color = color
        self.nbPage = nbPage
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

