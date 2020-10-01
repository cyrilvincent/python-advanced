import unittest
import media
import datetime
import logging

class MediaTest(unittest.TestCase):

    def test_first(self):
        logging.basicConfig(filename="log.txt")
        self.assertEqual(0, media.Book.nbBook())
        b1 = media.Book("Python", 10.0)
        self.assertEqual(1, media.Book.nbBook())
        b2 = media.Book("Numpy", 20, datetime.datetime(2020,9,30,16,8),"red",authors = ["Cyril","Toto"],nbPage=90)
        self.assertEqual(2, media.Book.nbBook())
        del(b2)
        self.assertEqual(1, media.Book.nbBook())
        self.assertAlmostEqual(10.03249, b1.netPrice(), delta=1e-3)
        b1.price = 20
        self.assertEqual(20, b1.price)
        with self.assertRaises(ValueError):
            logging.error("Price < 0")
            b1.price = -10

    def test_publisher(self):
        p1 = media.Publisher("Mon éditeur")
        b1 = media.Book("Python", 10,publisher = p1)
        self.assertEqual("Mon éditeur", b1.publisher.name)
        cart = media.Cart() # Cart ->* Book
        cart.add(b1)
        b2 = media.Book("Numpy", 20, publisher=p1)
        cart.add(b2)
        self.assertEqual(2, cart.nbItem)
        self.assertEqual((10+20)*1.055*0.95+0.01*2, cart.totalNetPrice)
        cart.remove(b2)
        self.assertEqual(1, cart.nbItem)
        self.assertEqual(10 * 1.055*0.95+0.01, cart.totalNetPrice)
        cd1 = media.Cd("Allumez le feu",5,authors=["Johnny"],nbTrack=10)
        cart.add(cd1)
        self.assertEqual(10 * 1.055*0.95+0.01 + 5 * 1.2, cart.totalNetPrice)
        # cd1.__dict__["title"] = "XXX"
        # print(cd1.__dict__["title"])
        # cd1.__dict__["toto"] = "titi"
        cd1 = media.Cd("Allumez le feu", 5, authors=["Johnny"], nbTrack=10)
        cd2 = media.Cd("Allumez le feu", 5, authors=["Johnny"], nbTrack=10)
        #Redéfinir == et != pour Media
        # Tester == et is
        # Tester cd2 in cart.items => True
        # cd1 == cd2
        # cd1 is cd2


