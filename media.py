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




