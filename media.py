from dataclasses import dataclass
from typing import List

@dataclass
class Publisher:

    name:str
    address:str=""

class Book:

    tva = 0.055

    def __init__(self, isbn:str, title:str, price:float, authors:List[str], type:str="", nb_page:int=0):
        self.isbn = isbn
        self.title = title
        self._price = price
        self.authors = authors
        self.type = type
        self.nb_page = nb_page

    def net_price(self):
        return self._price * (1 + 0.055)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price <= 0")

    @dataclass()
    def __del__(self):
        pass
        # Dernière méthode appelée avant destruction de l'objet




