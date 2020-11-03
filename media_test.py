import unittest
import media

class MediaTest(unittest.TestCase):

    def test_book(self):
        b1 = media.Book("123", "Python",10,["Cyril"],99)
        self.assertAlmostEqual(10.55,b1.net_price(),delta=1e-3)
