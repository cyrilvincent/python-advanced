import unittest
import rappels
import geometry
import media

class MyTests(unittest.TestCase):

    def test_debile(self):
        self.assertEqual(3, 1+2)
        my_bool = 1 < 2
        self.assertTrue(my_bool)

    def test_round(self):
        a = 2 ** 0.5
        self.assertAlmostEqual(1.414, a, delta=0.001)
        b = a ** 2
        self.assertAlmostEqual(2, b, delta=0.001)

    def test_is_prime(self):
        self.assertTrue(rappels.is_prime(7))
        self.assertFalse(rappels.is_prime(8))

    def test_filter_prime(self):
        l = [1,3,8,99,100,10,13,17,2,18]
        res = rappels.filter_prime(l)
        self.assertEqual([3,13,17,2], res)

    # def test_tp_filter_prime(self):
    #     l = [1, 3, 8, 99, 100, 10, 13, 17, 2, 18]
    #     res = tp_intention.filter_prime_x2(l)
    #     self.assertEqual([6,26,34,4], res)

    def test_geometry(self):
        r = geometry.Rectangle(3,2)
        self.assertEqual(6, r.get_area())
        self.assertEqual(10, r.get_perimeter())
        r2 = geometry.Rectangle(4,3)
        self.assertEqual(6, r.area)
        r.width = 4
        r2 = geometry.Rectangle2(length=3,width=4)
        print(r2.area())


    def test_media_book(self):
        book = media.Book("Python", 10.0)
        self.assertEqual("Python", book.title)
        # self.assertAlmostEqual(10.55, book.get_net_price(), delta=0.01)
        # book.get_net_price()
        # # <=>
        # media.Book.get_net_price(book)

    def test_nb_book(self):
        # Passer get_net_price en propriété
        book = media.Book("Python", 10.0)
        self.assertAlmostEqual(10.55, book.net_price, delta=0.01)
        b2 = media.Book("Numpy", 10)
        self.assertEqual(2, media.Book.nb_book)
        del(b2)
        self.assertEqual(1, media.Book.nb_book)

    def test_association(self):
        publisher = media.Publisher("Editions Python") # dataclass
        author1 = media.Author("Cyril", "Vincent", id="1234", mail="contact@cyrilvincent.com") # dataclass
        author2 = media.Author("Guido", "Van Rossum", id="007", mail="guido@microsoft.com")
        book = media.Book("Python", 10.0, publisher=publisher, authors=???)
        self.assertEqual("Editions Python", book)
        self.assertEqual("Guido", book.)




