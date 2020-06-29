class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def getPerimeter(self):
        return 2 * (self.length + self.width)

import unittest
class RectangleTest(unittest.TestCase):

    def test1(self):
        r1 = Rectangle(3,2)
        self.assertEqual(3, r1.length)
        self.assertEqual(2, r1.width)
        self.assertEqual(6, r1.getArea())
        self.assertEqual(10, r1.getPerimeter())
        r1.width+=1
        self.assertEqual(9, r1.getArea())
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

        area = r1.getArea()
        area = Rectangle.getArea(r1)





