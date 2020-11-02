import unittest
import geometry

class GeometryTest(unittest.TestCase):

    def test_rectangle(self):
        r1 = geometry.Rectangle(3,2)
        self.assertEqual(3, r1.width)
        self.assertEqual(2, r1.length)
        self.assertEqual(10, r1.perimeter())
        self.assertEqual(6, r1.area())