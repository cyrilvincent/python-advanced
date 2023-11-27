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

    def test_media_book(self):
        book = media.Book("Python", 10.0)
        self.assertEqual("Python", book.title)
        self.assertAlmostEqual(10.55, book.get_net_price(), delta=0.01)




