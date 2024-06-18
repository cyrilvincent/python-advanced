from dataclasses import dataclass
import math
import abc

@dataclass
class Coord:

    x: float
    y: float


class Polygon(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self): ...



class Rectangle(Polygon):

    def __init__(self, width: float, length: float, coord: Coord = Coord(0, 0)):
        self.width = width
        self.length = length
        self.coord = coord

    @property
    def area(self):
        return self.width * self.length

    def _perimeter(self):
        return 2 * (self.width + self.length)

    def move(self, coord: Coord):
        self.coord = coord

    def move_rel(self, x, y):
        self.coord.x += x
        self.coord.y += y


class Square(Rectangle):

    def __init__(self, side: float):
        super().__init__(side, side)


class TriangleRectangle(Rectangle):

    def __init__(self, width, length):
        super().__init__(width, length)

    @property
    def hypothenuse(self):
        return math.sqrt(self.width ** 2 + self.length ** 2)

    @property
    def area(self):
        return super().area / 2

    def _perimeter(self):
        return self.length + self.width + self.hypothenuse



