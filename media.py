# dataclass Publisher : Name, id
# 1 book possède 1 publisher
# dataclass Author fname, lname
# 1 book possède n authors
# Test
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import List



@dataclass
class Publisher:

    id: str
    name: str


@dataclass
class Author:

    first_name: str
    name: str


class Media(metaclass=ABCMeta):

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
    @abstractmethod
    def net_price(self):...

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
    nb_book = 0

    def __init__(self, title: str, price: float, isbn: str, authors: List[Author] = [], publisher: Publisher = None,
                 format="A4", nb_page=0):
        super().__init__(title, price, isbn, authors, publisher)
        self.format = format
        self.nb_page = nb_page
        Book.nb_book += 1


    @property
    def net_price(self):
        return self.price * (1 + Book.vat_rate)



class Cd(Media):

    def __init__(self, title: str, price: float, id: str, authors: List[Author] = [], publisher: Publisher = None,
                 nb_track=0):
        super().__init__(title, price, id, authors, publisher)
        self.nb_track = nb_track

    @property
    def net_price(self):
        return self.price * (1 + Media.vat_rate)

class Cart:

    def __init__(self):
        self.items: List[Media] = []

    def add(self, media: Media):
        self.items.append(media)

    def remove(self, media: Media):
        self.items.remove(media)

    @property
    def total_net_price(self):
        return sum([m.net_price for m in self.items])



