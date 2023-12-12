import math
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
        if self.width > self.length:
            raise ValueError("Width > Length")
        if not isinstance(origin, Point):
            raise TypeError("Type error")

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return 2 * (self.length + self.width)

    def __repr__(self):
        return f"{type(self)}: {self.length}x{self.width}"

class Square(Rectangle):

    def __init__(self, origin: Point, side):
        super().__init__(origin, side, side)


class Point3d(Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

class Triangle:

    def __init__(self, p1: Point, p2: Point, p3:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

class TriangleRectangle(Rectangle, Triangle):

    def __init__(self, origin: Point, length: float, width: float):
        super().__init__(origin, length, width)

    @property
    def area(self):
        return super().area / 2

    @property
    def hypothenuse(self):
        return math.sqrt(self.width ** 2 + self.length ** 2)

    @property
    def perimeter(self):
        return self.width + self.length + self.hypothenuse




