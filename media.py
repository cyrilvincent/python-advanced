class Book:

    def __init__(self, ean: str, title: str, price: float, genre: str = "", nb_page: int = 0):
        self.ean = ean
        self.title = title
        self.price = price
        self.genre = genre
        self.nb_page = nb_page

    def net_price(self) -> float:
        return self.price * 1.055

