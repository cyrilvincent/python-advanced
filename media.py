import datetime

class Book:

    def __init__(self, title, price, publicationDate = datetime.datetime.now(), color = "", authors = [], nbPage = 0):
        self.title = title
        self._price = price
        self.publicationDate = publicationDate
        self.color = color
        self.nbPage = nbPage

    def netPrice(self):
        return self._price * 1.055

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
        pass

