class Book:

    def __init__(self, id, title):
        self.id = id
        self.title = title

b1 = Book(1,"Python")
print(b1.__dict__)
dico = {'id':2, 'title':"Sale", "toto":"titi", "price":10}
b1.__dict__ = dico
print(b1.toto)
b1.__dict__["price"]+=1
b1.__dict__ = {
    "author": "Hans Christian Andersen",
    "country": "Denmark",
    "imageLink": "images/fairy-tales.jpg",
    "language": "Danish",
    "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
    "pages": 784,
    "title": "Fairy tales",
    "year": 1836
  }
print(b1.year)
