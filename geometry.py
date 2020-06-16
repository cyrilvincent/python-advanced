import unittest

class Rectangle:

    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

class GeometryTest(unittest.TestCase):

    def testRectangle(self):
        r1 = Rectangle(3,2)
        self.assertEqual(6, r1.getArea())
        self.assertEqual(10, r1.getPerimeter())
