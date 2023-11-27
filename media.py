from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Publisher:

    name: str

@dataclass
class Author:

    id: str
    first_name: str
    last_name: str
    mail: str


class Book:

    nb_book = 0

    def __init__(self, title, price, parution=datetime.now(), nb_page=0, publisher:Publisher=None, authors: List[Author]=[]):
        self.title = title
        self.price = price
        self.parution = parution
        self.nb_page = nb_page
        self.publisher = publisher
        self.authors = authors
        Book.nb_book += 1

    @property
    def net_price(self):
        return self.price * 1.055

    def __del__(self):
        Book.nb_book -= 1



