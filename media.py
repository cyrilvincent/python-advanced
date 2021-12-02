from dataclasses import dataclass


@dataclass
class Book:

    id: int
    title: str
    price: float
    nb_page: int = 0