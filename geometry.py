class Point:

    def __init__(self, x = 0, y = 0):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self.__eq__(other))
        # != n'est pas forcement égal à not(==)

import abc
class Polygon(metaclass=abc.ABCMeta):

    def __init__(self, origin=Point()):
        self.origin = origin

    @abc.abstractmethod
    def area(self):...

    @abc.abstractmethod
    def perimeter(self):...

class Rectangle(Polygon):

    toto = 3

    def __init__(self, length:float, width:float, origin:Point=Point()):
        super().__init__(origin)
        self.length = length
        self.width = width
        Rectangle.toto = 4

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    @staticmethod
    def static():
        return 0

    def move(self, x, y):
        self.origin.move(x,y)

    def __repr__(self):
        return f"Rectangle {self.length}x{self.width} {self.origin.__repr__()}"

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width and self.origin == other.origin

    def __ne__(self, other):
        return not(self.__eq__(other))

class Square(Rectangle):

    def __init__(self, side=0, origin=Point()):
        super().__init__(side, side, origin)
        self.toto = 0

import unittest
class RectangleTest(unittest.TestCase):

    def test1(self):
        r1 = Rectangle(3,2)
        self.assertEqual(3, r1.length)
        self.assertEqual(2, r1.width)
        self.assertEqual(6, r1.area)
        self.assertEqual(10, r1.perimeter)
        r1.width+=1
        self.assertEqual(9, r1.area)
        r1 = Rectangle(3,2)
        r2 = Rectangle(3,2)
        self.assertNotEqual(r1, r2)
        print(r1)
        print(r2)
        r1 = r2
        print(r1)
        print(r2)
        r1.width+=1
        self.assertEqual(r1, r2)

    def test2(self):
        r1 = Rectangle(3,2)
        r2 = Rectangle(4,6)
        r1.width = 99
        r2.width = 98

        area = r1.area
        #area = Rectangle.area(r1)

    def testStatic(self):
        Rectangle.toto = 5
        r1 = Rectangle(0,0)
        print(r1.toto)
        r2 = Rectangle(0,0)

    def testPoint(self):
        p1 = Point(0,0)
        print(p1)
        r1 = Rectangle(0,0,p1)
        r2 = Rectangle(0,0,Point(0,0))
        r1.move(3,2)
        self.assertEqual(3, r1.origin.x)
        print(r1.__dir__())

    def testSquare(self):
        c = Square(2)
        self.assertEqual(4, c.area)

    def testAbc(self):
        r = Rectangle(3,2)
        print(r)

    def testEqualityPoint(self):
        p1 = Point(3,2)
        p2 = Point(3,2)
        self.assertTrue(p1 == p2)
        #15h45







