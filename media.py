from dataclasses import dataclass
from typing import List

@dataclass
class Publisher:

    name:str
    address:str=""

class Book:

    tva = 0.055
    nb_book = 0

    def __init__(self, isbn:str, title:str, price:float, authors:List[str], type:str="", nb_page:int=0, publisher:Publisher = None):
        self.isbn = isbn
        self.title = title
        self._price = price
        self.authors = authors
        self.type = type
        self.nb_page = nb_page
        self.publisher = publisher
        Book.nb_book += 1

    def net_price(self):
        return self._price * (1 + Book.tva)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price <= 0")

    def __del__(self):
        Book.nb_book -= 1

class Cart:

    def __init__(self):
        self.items:List[Book] = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def total_net_price(self):
        sum = 0
        for item in self.items:
            sum += item.net_price()
        return sum




