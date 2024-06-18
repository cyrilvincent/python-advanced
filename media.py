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


class Book:

    tva = 0.055
    nb_book = 0

    def __init__(self, ean: str, title: str, price: float, genre: str = "", nb_page: int = 0,
                 publisher: Publisher = None, authors: list[Author] = []):
        self.ean = ean
        self.title = title
        self.price = price
        self.genre = genre
        self.nb_page = nb_page
        self.publisher = publisher
        self.authors = authors
        Book.nb_book += 1

    def net_price(self) -> float:
        return self.price * (1 + Book.tva)

    def __del__(self):
        Book.nb_book -= 1
