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


class Media:

    nb_media = 0
    vat_rate = 0.2

    def __init__(self, title: str, price: float, id: str, authors: List[Author] = [], publisher: Publisher = None):
        self.title = title
        self.price = price
        self.id = id
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    @property
    def net_price(self):
        return self.price * (1 + Media.vat_rate)

    def __del__(self):
        Media.nb_media -= 1
        # x = y => x va mourir
        # x = None
        # del(x)

 # Créer la classe Cd(nb_track) et Dvd(zone)
 # Penser à faire un Media
 # Penser au prixTTC Book 5.5%, le reste 20%
 # Reprise à 10h45

class Book(Media):

    vat_rate = 0.055

    def __init__(self, title: str, price: float, isbn: str, authors: List[Author] = [], publisher: Publisher = None,
                 format="A4", nb_page=0):
        super().__init__(title, price, isbn, authors, publisher)
        self.format = format
        self.nb_page = nb_page


    @property
    def net_price(self):
        return self.price * (1 + Book.vat_rate)

class Cd(Media):

    def __init__(self, title: str, price: float, id: str, authors: List[Author] = [], publisher: Publisher = None,
                 nb_track=0):
        super().__init__(title, price, id, authors, publisher)
        self.nb_track = nb_track

