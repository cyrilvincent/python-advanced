import unittest
import tp1
import geometry
import media

class MyTests(unittest.TestCase):

    def test_first(self):
        self.assertEqual(2, 1+1)

    def test_float(self):
        self.assertAlmostEqual(1.414, 2 ** 0.5, delta=1e-3)

    def test_is_prime(self):
        self.assertTrue(tp1.is_prime(7))
        self.assertFalse(tp1.is_prime(9))

    def test_rectangle(self):
        r = geometry.Rectangle(2, 3)
        self.assertEqual(6, r.area)
        self.assertEqual(10, r._perimeter())


    def test_book(self):
        b = media.Book("1", "Python", 10)
        self.assertAlmostEqual(10.55, b.net_price(), delta=1e-3)
        self.assertAlmostEqual(10.55, media.Book.net_price(b))

    def test_coord(self):
        c = geometry.Coord(1,4)
        r = geometry.Rectangle(2,3,c)
        self.assertEqual(1, r.coord.x)

    def test_publisher(self):
        p = media.Publisher(1, "Cyril")
        b = media.Book("1","Python",10,publisher=p)
        b2 = media.Book("1","Python",10, publisher=media.Publisher(1, "Cyril"))
        self.assertEqual("Cyril", b.publisher.name)

    def test_authors(self):
        a1 = media.Author("Cyril", "Vincent")
        a2 = media.Author("Victor", "Hugo")
        b = media.Book("1","Python",10,authors=[a1, a2])
        self.assertEqual("Cyril", b.authors[0].first_name)

    def test_nb_book(self):
        b = media.Book("","",0)
        self.assertEqual(1, b.nb_book)
        b2 = media.Book("", "", 0)
        self.assertEqual(2, b.nb_book)
        del b2
        self.assertEqual(1, b.nb_book)

    def test_square(self):
        s = geometry.Square(3)
        self.assertEqual(9, s.area)
        self.assertEqual(12, s._perimeter())
