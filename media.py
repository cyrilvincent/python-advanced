from dataclasses import dataclass
from typing import Optional, List
import abc
import pickle
import jsonpickle
import re


@dataclass
class Publisher:

    id: int
    name: str

class IMedia(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def net_price(self): ...


class AbstractMedia(IMedia):

    taxe = 0.2

    def __init__(self, id, title, price, publisher: Optional[Publisher] = None):
        self.id = id
        self.title = title
        self.price = price
        self.publisher = publisher

    @property
    def net_price(self):
        return self.price * (1 + AbstractMedia.taxe)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Cd(AbstractMedia):

    def __init__(self, id, title, price, publisher: Optional[Publisher] = None, nb_track=0):
        super().__init__(id, title, price,publisher)
        self.nb_track = nb_track


class Book(AbstractMedia):

    taxe = 0.05

    def __init__(self, id, title, price, publisher: Optional[Publisher] = None, nb_page=0):
        super().__init__(id, title, price,publisher)
        self.nb_page = nb_page
        self._isbn = None

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        regex = r"^\d{3}-\d-\d{4}-\d{4}-\d$"
        if re.match(regex, value):
            self._isbn = value
        else:
            raise ValueError("Bad ISBN format")

    @property
    def net_price(self)->float:
        """
        calcul de prix TTC
        :return:
        """
        return self.price * 0.95 * (1 + Book.taxe) + 0.01

class Cart:

    def __init__(self):
        self.medias:List[AbstractMedia] = []

    def add(self, media:AbstractMedia):
        self.medias.append(media)

    def remove(self, media:AbstractMedia):
        self.medias.remove(media)

    @property
    def total_net_price(self)->float:
        """
        Calcul le prix TTC du panier
        :return: le prix
        """
        return sum([m.net_price for m in self.medias])


class AbstractMediaRepository(metaclass=abc.ABCMeta):


    def __init__(self, medias):
        """
        Constructeur
        :param medias: liste des medias
        """
        self.medias = medias

    @abc.abstractmethod
    def save(self, uri): ...

    @abc.abstractmethod
    def load(self, uri): ...


class JsonMediaRepository(AbstractMediaRepository):

    def __init__(self, medias):
        super().__init__(medias)

    def save(self, uri, unpicklable=False):
        with open(uri, "w") as f:
            f.write(jsonpickle.encode(self.medias, unpicklable=unpicklable, indent=4))

    def load(self, uri):
        with open(uri, "r") as f:
            self.medias = jsonpickle.decode(f.read())

class PickleMediaRepository(AbstractMediaRepository):

    def __init__(self, medias):
        super().__init__(medias)

    def save(self, uri):
        with open(uri, "w") as f:
            pickle.dump(self.medias, f)

    def load(self, uri):
        with open(uri, "r") as f:
            self.medias = pickle.load(f)

