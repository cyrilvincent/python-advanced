import abc
import csv
from dataclasses import dataclass
from datetime import datetime
from typing import List
from abc import ABCMeta, abstractmethod


@dataclass
class Publisher:

    name: str

@dataclass
class Author:

    id: str
    first_name: str
    last_name: str
    mail: str


class Media(metaclass=ABCMeta):

    nb_media = 0

    def __init__(self,
                 title,
                 price,
                 parution=datetime.now(),
                 publisher:Publisher=None,
                 authors: List[Author]=[]):
        self.title = title
        self.price = price
        self.parution = parution
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    @abstractmethod
    def net_price(self):...

    def __del__(self):
        Media.nb_media -= 1

class Book(Media):

    def __init__(self,
                 title,
                 price,
                 parution=datetime.now(),
                 publisher: Publisher = None,
                 authors: List[Author] = [],
                 nb_page=0):
        super().__init__(title, price, parution, publisher, authors)
        self.nb_page = nb_page

    def __repr__(self):
        return f"Book: {self.title} {self.price}"

    @property
    def net_price(self):
        return self.price * 1.2 * 0.95 + 0.01


class Cd(Media):
    def __init__(self,
                 title,
                 price,
                 parution=datetime.now(),
                 publisher: Publisher = None,
                 authors: List[Author] = [],
                 nb_track=0):
        super().__init__(title, price, parution, publisher, authors)
        self.nb_track = nb_track

    @property
    def net_price(self):
        return self.price * 1.2

class AbstractMediaService(metaclass=abc.ABCMeta):

    def __init__(self):
        self.medias: List[Media]= []

    @abstractmethod
    def load(self, path: str):...

    @abstractmethod
    def get_by_title(self, title: str) -> List[Media]:...
        # "th".upper() in "python".upper() => True
        # Intention list
        # UnitTest

    @abstractmethod
    def get_by_price(self, price: float) -> List[Media]:...
        # Retourne les livres <= price

    @abstractmethod
    def add(self, m: Media):...

    # Faire un moteur de recherche de livre
    # Saisir le prix du livre ou son titre
    # Checkbox pour choisir title ou price
    # Afficher le 1er résultat dans un label
    # Bonus : ListBox (items) => Title des livres trouvés

class MediaService(AbstractMediaService):

    def __init__(self):
        super().__init__()

    def load(self, path: str):
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row["title"]
                price = float(row["price"])
                b = Book(title, price)
                self.medias.append(b)

    def get_by_price(self, price: float) -> List[Media]:
        return [b for b in self.medias if b.price <= price]

    def get_by_title(self, title: str) -> List[Media]:
        return [b for b in self.medias if title.upper() in b.title.upper()]

    def add(self, m: Media):
        self.medias.append(m)







