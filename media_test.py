import unittest
import media

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
        b1 = media.Book("123", "Python", 10, ["Cyril"], 99)
        b2 = media.Book("123", "Python", 10, ["Cyril"], 99)
        b1._price = 0
        self.assertNotEqual(b1, b2)
        self.assertIsNot(b1, b2)
        b1 = b2
        self.assertEqual(b1, b2)
        self.assertIs(b1, b2)
        b1 = None #Rare
        del(b1) #Rare

    def test_publisher(self):
        p1 = media.Publisher("ENI", "Champs Elysée, Paris")
        self.assertEqual(p1.name, "ENI")
