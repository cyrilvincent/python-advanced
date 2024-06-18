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


@dataclass
class Publisher:

    id: int
    name: str

@dataclass
class Author:

    first_name: str
    last_name: str


class Media:

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

    def net_price(self) -> float:
        return self.price * (1 + Media.tva)

    def __del__(self):
        Media.nb_media -= 1


class Book(Media):

    tva = 0.055

    def __init__(self, ean: str, title: str, price: float, genre: str = "",
                 publisher: Publisher = None, authors: list[Author] = [], nb_page=0):
        super().__init__(ean, title, price, genre, publisher, authors)
        self.nb_page = nb_page

    def net_price(self) -> float:
        return self.price * (1 + Book.tva)


class Cd(Media):

    def __init__(self, ean: str, title: str, price: float, genre: str = "",
                 publisher: Publisher = None, authors: list[Author] = [], nb_track=0):
        super().__init__(ean, title, price, genre, publisher, authors)
        self.nb_track = nb_track


