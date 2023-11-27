from datetime import datetime


class Book:

    def __init__(self, title, price, parution=datetime.now(), nb_page=0):
        self.title = title
        self.price = price
        self.parution = parution
        self.nb_page = nb_page

    def get_net_price(self):
        return self.price * 1.055

