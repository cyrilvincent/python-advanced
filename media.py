# dataclass Publisher : Name, id
# 1 book possède 1 publisher
# dataclass Author fname, lname
# 1 book possède n authors
# Test
from dataclasses import dataclass
from typing import List


@dataclass
class Publisher:

    id: str
    name: str


@dataclass
class Author:

    first_name: str
    last_name: str


class Book:

    nb_book = 0
    vat_rate = 0.055

    def __init__(self, title: str, price: float, isbn: str, authors: List[Author] = [], publisher: Publisher = None,
                 format="A5", nb_page=0):
        self.title = title
        self.price = price
        self.isbn = isbn
        self.format = format
        self.nb_page = nb_page
        self.publisher = publisher
        self.authors = authors
        self._toto = 0
        Book.nb_book += 1

    @property
    def net_price(self):
        return self.price * (1 + Book.vat_rate)

    def __del__(self):
        Book.nb_book -= 1
        # x = y => x va mourir
        # x = None
        # del(x)

    # Mettre le taux de TVA en static
    # Compter automatiquement les livres
