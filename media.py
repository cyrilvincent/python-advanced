# Créer la dataclass Publisher
# Ajouter l'attribut book.publisher (relation 1)
# Créer la dataclass Author
# Ajouter l'attribut book.authors (relation n)
# Tester

# Mettre la TVA en variable statique
# Compter automatiquement le nombre de livre instancié

# Créer les classes cd(nb_track) dvd(zone)
# Pour celà créer la super classe Media
# Garder Book.tva = 5.5%
# Créer Media.tva = 20%
# Tester

from dataclasses import dataclass
import abc


@dataclass
class Publisher:

    id: int
    name: str

@dataclass
class Author:

    first_name: str
    last_name: str


class Media(metaclass=abc.ABCMeta):

    tva = 0.2
    nb_media = 0

    def __init__(self, ean: str, title: str, price: float, genre: str = "",
                 publisher: Publisher = None, authors: list[Author] = []):
        self.ean = ean
        self.title = title
        self.price = price
        self.genre = genre
        self.publisher = publisher
        self.authors = authors
        Media.nb_media += 1

    @abc.abstractmethod
    def net_price(self) -> float: ...

    def __eq__(self, other):
        return self.ean == other.ean

    def __del__(self):
        Media.nb_media -= 1

    def __repr__(self):
        return f"{type(self).__name__} {self.ean} {self.title} {self.price}"


class Book(Media):

    tva = 0.055

    def __init__(self, ean: str, title: str, price: float, genre: str = "",
                 publisher: Publisher = None, authors: list[Author] = [], nb_page=0):
        super().__init__(ean, title, price, genre, publisher, authors)
        self.nb_page = nb_page

    def net_price(self) -> float:
        return self.price * 0.95 * (1 + Book.tva) + 0.01


class Cd(Media):

    def __init__(self, ean: str, title: str, price: float, genre: str = "",
                 publisher: Publisher = None, authors: list[Author] = [], nb_track=0):
        super().__init__(ean, title, price, genre, publisher, authors)
        self.nb_track = nb_track

    def net_price(self) -> float:
        return self.price * (1 + Media.tva)


class Dvd(Media):

    def __init__(self, ean: str, title: str, price: float, genre: str = "",
                 publisher: Publisher = None, authors: list[Author] = [], zone=0):
        super().__init__(ean, title, price, genre, publisher, authors)
        self.zone = zone

    def net_price(self) -> float:
        return self.price * (1 + Media.tva) * 0.5


class Cart:

    def __init__(self):
        self.items: list[Media] = []

    def add(self, media: Media):
        self.items.append(media)

    def remove(self, media: Media):
        self.items.remove(media)

    def validate(self) -> bool:
        return True

    def total_net_price(self) -> float:
        return sum([m.net_price() for m in self.items])

if __name__ == '__main__':
    b = Book("1", "Python", 10)
    dico = b.__dict__
    print(dico["title"])
    dico["title"] = "toto"
    print(b.title)
    b2 = Book("1", "Python", 10)
    print(b == b2)
    print(b)


