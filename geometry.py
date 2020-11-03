from dataclasses import dataclass
import math

@dataclass
class Point:

    x : float = 0
    y : float = 0



class Rectangle:

    def __init__(self, width:float=0, length:float=0, origin:Point = Point()):
        self._width = width
        self._length = length
        self.origin = origin


    def perimeter(self):
        return 2 * (self._length + self._width)

    def area(self):
        return self._length * self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
        else:
            raise ValueError("Width < 0")

    def move(self, x:float, y:float):
        self.origin.x = x
        self.origin.y = y

@dataclass
class Circle:

    radius : float

    def area(self):
        return math.pi * self.radius ** 2



