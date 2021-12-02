from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from typing import List, ClassVar


@dataclass
class Media(metaclass=ABCMeta):

    id: int
    title: str
    price: float
    nb_media: ClassVar[int]
    TYPE: int = 1

    @abstractmethod
    def net_price(self):...

@dataclass
class Dvd(Media):

    zone: int

    @property
    def net_price(self):
        return self.price * 1.2

@dataclass
class Book(Media):

    nb_page: int = 0

    @property
    def net_price(self):
        return 0.01 + self.price * 1.05 * 0.95

class CartService:

    nb_cart: int = 0

    def __init__(self):
        self.medias: List[Media] = []
        CartService.nb_cart += 1

    def add(self, media: Media):
        self.medias.append(media)

    def remove(self, media: Media):
        if media in self.medias:
            self.medias.remove(media)

    def get_total_net_price(self):
        return sum([m.net_price for m in self.medias])

    def __del__(self):
        CartService.nb_cart -= 1

