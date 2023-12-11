from dataclasses import dataclass

@dataclass
class Point:

    x: float
    y: float

class Rectangle:

    def __init__(self, origin: Point, length, width=0):
        self.origin = origin
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)


