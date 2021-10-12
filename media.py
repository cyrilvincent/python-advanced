from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Publisher:

    id: int
    name: str


class Media:

    taxe = 0.2

    def __init__(self, id, title, price, publisher: Optional[Publisher] = None):
        self.id = id
        self.title = title
        self.price = price
        self.publisher = publisher

    @property
    def net_price(self):
        return self.price * (1 + Media.taxe)


class Cd(Media):

    def __init__(self, id, title, price, publisher: Optional[Publisher] = None, nb_track=0):
        super().__init__(id, title, price,publisher)
        self.nb_track = nb_track


class Book(Media):

    taxe = 0.05

    def __init__(self, id, title, price, publisher: Optional[Publisher] = None, nb_page=0):
        super().__init__(id, title, price,publisher)
        self.nb_page = nb_page

    @property
    def net_price(self):
        return self.price * 0.95 * (1 + Book.taxe) + 0.01

class Cart:

    def __init__(self):
        self.medias:List[Media] = []

    def add(self, media:Media):
        self.medias.append(media)

    def remove(self, media:Media):
        self.medias.remove(media)

    @property
    def total_net_price(self):
        return sum([m.net_price for m in self.medias])