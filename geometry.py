from typing import List

class Coord:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

class Rectangle:

    def __init__(self, length=0.0, width=0.0, coord=Coord()):
        self._length: float = length
        self.width:float = width
        self.coord: Coord = coord

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    def perimeter(self):
        return 2 * (self.width + self._length)

    @property
    def area(self):
        return self._length * self.width

    def move(self, x, y):
        self.coord.x = x
        self.coord.y = y

    def __del__(self):
        pass

class Rectangles:

    def __init__(self):
        self.rectangles: List[Rectangle] = []

