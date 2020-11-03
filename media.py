from dataclasses import dataclass
from typing import List

@dataclass
class Publisher:

    name:str
    address:str=""

class Media:

    tva = 0.2

    def __init__(self, id:str, title:str, price:float, authors:List[str], type:str= "", publisher:Publisher = None):
        self.id = id
        self.title = title
        self._price = price
        self.authors = authors
        self.type = type
        self.publisher = publisher

    def net_price(self):
        return self._price * (1 + Media.tva)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price <= 0")

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

class Book(Media):

    tva = 0.055
    nb_book = 0

    def __init__(self, id:str, title:str, price:float, authors:List[str], type:str="", nb_page:int=0, publisher:Publisher = None):
        super().__init__(id,title,price,authors,type,publisher)
        self.nb_page = nb_page
        Book.nb_book += 1

    def net_price(self):
        return self._price * (1 + Book.tva)

    def __del__(self):
        Book.nb_book -= 1

class Cd(Media):

    def __init__(self, id:str, title:str, price:float, authors:List[str], type:str="", nb_track:int=0, publisher:Publisher = None):
        super().__init__(id,title,price,authors,type,publisher)
        self.nb_track = nb_track

class Cart:

    def __init__(self):
        self.items:List[Media] = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def total_net_price(self):
        sum = 0
        for item in self.items:
            sum += item.net_price()
        return sum




