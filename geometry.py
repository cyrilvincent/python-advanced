import unittest

class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def move(self, x, y):
        self.x = x
        self.y = y

    def moveRel(self, x, y):
        self.x += x
        self.y += y


class Rectangle:

    def __init__(self, length = 0, width = 0, origin = Point()):
        self._length = length
        self._width = width
        self.origin = origin

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

    def move(self, x, y):
        self.origin.move(x,y)

    def __repr__(self):
        return f"Rectangle {self.origin} L{self.length} W{self._width}"

class GeometryTest(unittest.TestCase):

    def testRectangle(self):
        r1 = Rectangle(3,2,Point(4,2))
        self.assertEqual(6, r1.area)
        self.assertEqual(10, r1.perimeter)
        r1.move(5,2)
        r1.origin.moveRel(1,1)
        print(r1)

    def testPoint(self):
        p1 = Point(3,2)
        p1.move(4,3)
        self.assertEqual(4, p1.x)
        self.assertEqual(3, p1.y)
        print(p1)
        p1.moveRel(-1,-1)
        self.assertEqual(3, p1.x)
        self.assertEqual(2, p1.y)