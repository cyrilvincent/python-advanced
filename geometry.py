import unittest

class Rectangle:

    def __init__(self, length = 0, width = 0):
        self._length = length
        self._width = width
        # Passer les 2 attributs en propriétés ainsi que la surface et le périmètre

    @property
    def area(self):
        return self._length * self._width

    @property
    def perimeter(self):
        return 2 * (self._length + self._width)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

class GeometryTest(unittest.TestCase):

    def testRectangle(self):
        r1 = Rectangle(3,2)
        self.assertEqual(6, r1.area)
        self.assertEqual(10, r1.perimeter)
