# dataclass Publisher : Name, id
# 1 book possède 1 publisher
# dataclass Author fname, lname
# 1 book possède n authors
# Test

class Book:

    def __init__(self, title: str, price: float, isbn: str, format="A5", nb_page=0):
        self.title = title
        self.price = price
        self.isbn = isbn
        self.format = format
        self.nb_page = nb_page
        self._toto = 0

    @property
    def net_price(self):
        return self.price * 1.055

    def _titi(self):
        pass

