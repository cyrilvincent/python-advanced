# Créer la dataclass Publisher
# Ajouter l'attribut book.publisher (relation 1)
# Créer la dataclass Author
# Ajouter l'attribut book.authors (relation n)
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

    def __init__(self, ean: str, title: str, price: float, genre: str = "", nb_page: int = 0,
                 publisher: Publisher = None, authors: list[Author] = []):
        self.ean = ean
        self.title = title
        self.price = price
        self.genre = genre
        self.nb_page = nb_page
        self.publisher = publisher
        self.authors = authors

    def net_price(self) -> float:
        return self.price * 1.055

