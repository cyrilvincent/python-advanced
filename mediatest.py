import unittest
import media
import datetime
import logging

class MediaTest(unittest.TestCase):

    def test_first(self):
        logging.basicConfig(filename="log.txt")
        self.assertEqual(0, media.Book.nbBook)
        b1 = media.Book("Python", 10.0)
        self.assertEqual(1, media.Book.nbBook)
        b2 = media.Book("Numpy", 20, datetime.datetime(2020,9,30,16,8),"red",authors = ["Cyril","Toto"],nbPage=90)
        self.assertEqual(2, media.Book.nbBook)
        del(b2)
        self.assertEqual(1, media.Book.nbBook)
        self.assertAlmostEqual(10.55, b1.netPrice(), delta=1e-3)
        b1.price = 20
        self.assertEqual(20, b1.price)
        with self.assertRaises(ValueError):
            logging.error("Price < 0")
            b1.price = -10
        # Mieux gérer la TVA
        # Compter automatiquement le nombre d'instance de Book
