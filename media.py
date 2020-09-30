import datetime

class Book:

    def __init__(self, title, price, publicationDate = datetime.datetime.now(), color = "", authors = [], nbPage = 0):
        self.title = title
        self.price = price
        self.publicationDate = publicationDate
        self.color = color
        self.nbPage = nbPage

    def netPrice(self):
        return self.price * 1.055

