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
        self.assertAlmostEqual(10.032, b.net_price(), delta=1e-3)
        self.assertAlmostEqual(10.032, media.Book.net_price(b), delta=1e-3)

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
        self.assertEqual(1, b.nb_media)
        b2 = media.Book("", "", 0)
        self.assertEqual(2, b.nb_media)
        del b2
        self.assertEqual(1, b.nb_media)

    def test_square(self):
        s = geometry.Square(3)
        self.assertEqual(9, s.area)
        self.assertEqual(12, s._perimeter())

    def test_cd(self):
        cd = media.Cd("1", "Johnny", 10)
        self.assertAlmostEqual(12.0, cd.net_price(), delta=1e-3)

    def test_polymorphism(self):
        l: list[geometry.Rectangle] = []
        l.append(geometry.Rectangle(3,2))
        l.append(geometry.Square(3))
        l.append(geometry.TriangleRectangle(3,2))
        total = sum([r.area for r in l])

    def test_polygon(self):
        with self.assertRaises(TypeError):
            p = geometry.Polygon()

    def test_cart(self):
        cart = media.Cart()
        cart.add(media.Book("", "", 10))
        cart.add(media.Cd("", "", 10))
        cart.add(media.Dvd("", "", 10))
        self.assertAlmostEqual(28.032, cart.total_net_price(), delta=1e-3)

