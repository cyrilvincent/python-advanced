import unittest
import media
import datetime
import logging

class MediaTest(unittest.TestCase):

    def test_first(self):
        logging.basicConfig(filename="log.txt")
        b1 = media.Book("Python", 10.0)
        b2 = media.Book("Numpy", 20, datetime.datetime(2020,9,30,16,8),"red",authors = ["Cyril","Toto"],nbPage=90)
        self.assertAlmostEqual(10.55, b1.netPrice(), delta=1e-3)
        b1.price = 20
        self.assertEqual(20, b1.price)
        with self.assertRaises(ValueError):
            logging.error("Price < 0")
            b1.price = -10
