import unittest

class Rectangle:

    def __init__(self, length = 0, width = 0):
        self._length = length
        self.width = width
        # Passer les 2 attributs en propriétés ainsi que la surface et le périmètre

    def getArea(self):
        return self._length * self.width

    def getPerimeter(self):
        return 2 * (self._length + self.width)

    @property
    def length(self):
        return self._length
    
    @property
    def toto(self):
        return 
    
    @toto.setter
    def toto(self, value):
        pass

class GeometryTest(unittest.TestCase):

    def testRectangle(self):
        r1 = Rectangle(3,2)
        self.assertEqual(6, r1.getArea())
        self.assertEqual(10, r1.getPerimeter())
