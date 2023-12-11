# class Book
# Avec environ 5 attributs (dont title, price)
# net_price() => price * 1.055
# Tester AlmostEqual(delta=0.001)
# Reprise 15h

class Book:

    def __init__(self, title: str, price: float, isbn: str, format="A5", nb_page=0):
        self.title = title
        self.price = price
        self.isbn = isbn
        self.format = format
        self.nb_page = nb_page

    def net_price(self):
        return self.price * 1.055
