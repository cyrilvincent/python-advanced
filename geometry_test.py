import unittest
import geometry
import math

class GeometryTest(unittest.TestCase):

    def test_rectangle(self):
        r1 = geometry.Rectangle(3,2)
        #r1.width = r1.width + 1
        self.assertEqual(3, r1.width)
        self.assertEqual(2, r1._length)
        self.assertEqual(10, r1.perimeter())
        self.assertEqual(6, r1.area())

    def test_circle(self):
        c1 = geometry.Circle(1)
        self.assertAlmostEqual(math.pi, c1.area(),delta = 1e-3)