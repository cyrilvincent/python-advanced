from typing import List

class Book:

    def __init__(self, isbn:str, title:str, price:float, authors:List[str], type:str="", nb_page:int=0):
        self.isbn = isbn
        self.title = title
        self._price = price
        self.authors = authors
        self.type = type
        self.nb_page = nb_page

    def net_price(self):
        return self._price * (1 + 0.055)



