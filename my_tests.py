import unittest
import math

import demo_static
import rappels
import geometry
import media


class MyTests(unittest.TestCase):

    def test_first(self):
        self.assertEqual(2, 1+1)
        self.assertTrue(1 + 1 == 2)
        self.assertAlmostEqual(1.414, math.sqrt(2), delta=0.001)

    def test_is_prime(self):
        res = rappels.is_prime(7)
        self.assertTrue(res)
        self.assertFalse(rappels.is_prime(8))

    def test_filter_generic(self):
        l = [1, 2, 8, 7, 9, 12, 13, 99, 51, 11]
        res = rappels.filter_generic(rappels.is_prime, l)
        self.assertEqual([2, 7, 13, 11], res)


    def test_intention(self):
        l = [1,2,3,4,5,6,7,8,9]
        res = [x ** 2 for x in l if rappels.is_prime(x)]
        self.assertEqual([4,9,25,49], res)

    def test_rectangle(self):
        p1 = geometry.Point(2,-1)
        r1 = geometry.Rectangle(p1,3,2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.length, 3)
        self.assertEqual(r1.area, 6)
        self.assertEqual(r1.perimeter(), 10)
        r2 = geometry.Rectangle(geometry.Point(5,4), 4, 2)
        r2.width = 3
        r2.origin.x += 1

    def test_book(self):
        b1 = media.Book("Python", 10.0, "1234567890123")
        self.assertEqual("Python", b1.title)
        self.assertAlmostEqual(10.55, b1.net_price(), delta=0.001)

        b1.net_price() # <=> media.Book.net_price(b1)
        b1._toto = 4

    def test_point(self):
        p1 = geometry.Point(3,2)
        self.assertEqual(3, p1.x)
        self.assertEqual(2, p1.y)

    def test_publisher(self):
        p1 = media.Publisher("1", "Python.org")
        a1 = media.Author("Cyril", "Vincent")
        a2 = media.Author("Guido", "Van Rossum")
        b1 = media.Book("Python",10,"1234567890123", [a1, a2], p1)
        self.assertEqual("1", b1.publisher.id)
        b2 = media.Book("Python", 10, "1234567890123", [a1], media.Publisher("1", "Python.org"))
        self.assertEqual("Cyril", b1.authors[0].first_name)

    def test_nb_book(self):
        b1 = media.Book("Python",10,"1234567890123")
        self.assertEqual(media.Book.nb_book, 1)
        b2 = media.Book("Python 3", 10, "1234567890123")
        self.assertEqual(media.Book.nb_book, 2)
        del(b2)
        self.assertEqual(media.Book.nb_book, 1)

    def test_square(self):
        s = geometry.Square(geometry.Point(0,0), 3)
        print(s)
        self.assertEqual(9, s.area)
        self.assertEqual(12, s.perimeter)

    def test_robustness(self):
        with self.assertRaises(ValueError):
            r = geometry.Rectangle(geometry.Point(0,0), 0, 1)

    def test_triangle_rectangle(self):
        tr = geometry.TriangleRectangle(geometry.Point(0,0),3,2)
        self.assertEqual(3, tr.area)

    def test_cd(self):
        cd = media.Cd("Python Rock",10, "007")
        self.assertAlmostEqual(12, cd.net_price, delta=0.001)





