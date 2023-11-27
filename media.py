from datetime import datetime


class Book:

    nb_book = 0

    def __init__(self, title, price, parution=datetime.now(), nb_page=0):
        self.title = title
        self.price = price
        self.parution = parution
        self.nb_page = nb_page
        Book.nb_book += 1

    @property
    def net_price(self):
        return self.price * 1.055

    def __del__(self):
        Book.nb_book -= 1



