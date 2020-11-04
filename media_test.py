import unittest
import media
import pickle


class MediaTest(unittest.TestCase):

    def test_book(self):
        b1 = media.Book("123", "Python",10,["Cyril"],99)
        self.assertAlmostEqual(10.55,b1.net_price(),delta=1e-3)
        b1.net_price()
        # <=>
        media.Book.net_price(b1)

    def test_self(self):
        i = 1
        j = 1
        self.assertEqual(i,j)
        j += 1
        self.assertNotEqual(i, j)
        self.assertEqual(0, media.Book.nb_book)
        b1 = media.Book("123", "Python", 10, ["Cyril"], 99)
        self.assertEqual(1, media.Book.nb_book)
        b2 = media.Book("123", "Python", 10, ["Cyril"], 99)

        self.assertEqual(2, media.Book.nb_book)
        b1._price = 0
        self.assertEqual(b1, b2)
        self.assertIsNot(b1, b2)
        b1 = b2
        self.assertEqual(b1, b2)
        self.assertIs(b1, b2)
        b1 = None #Rare
        del(b1) #Rare
        self.assertEqual(1, media.Book.nb_book)


    def test_publisher(self):
        p1 = media.Publisher("ENI", "Champs Elysée, Paris")
        self.assertEqual(p1.name, "ENI")
        b1 = media.Book("123", "Python", 10, ["Cyril"],"Informatique", 99, p1)
        self.assertEqual("ENI", b1.publisher.name)

    def test_cart(self):
        cart = media.Cart()
        self.assertEqual(0, len(cart.items))
        b1 = media.Book("123", "Python", 10, ["Cyril"],"Informatique", 99)
        cart.add(b1)
        self.assertEqual(1, len(cart.items))
        b2 = media.Book("456", "Numpy", 20, ["Cyril"],"Informatique", 99)
        cart.add(b2)
        self.assertEqual(2, len(cart.items))
        self.assertAlmostEqual((10+20)*1.055, cart.total_net_price(),delta=1e-3)
        cart.remove(b2)
        self.assertEqual(1, len(cart.items))
        self.assertAlmostEqual((10) * 1.055, cart.total_net_price(),delta=1e-3)
        with open("cart.pickle","wb") as f:
            pickle.dump(cart, f)
        cart = None
        with open("cart.pickle","rb") as f:
            cart = pickle.load(f)
        print(cart)

    def test_inheritance(self):
        cd = media.Cd("001","Allumez le feu",10, ["Johnny"])
        self.assertAlmostEqual(12.0,cd.net_price(),delta = 1e-3)

    def test_dict(self):
        b1 = media.Book("123", "Python", 10, ["Cyril"], "Informatique", 99)
        print(b1.__dict__)
        b1.__dict__["id"]="456"
        self.assertEqual("456", b1.__dict__["id"])
        dico = {'id': '789', 'title': 'Python 3', '_price': 15, 'authors': ['Cyril'], 'type': 'Informatique', 'publisher': None, 'nb_page': 99}
        b1.__dict__ = dico
        print(b1)