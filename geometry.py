from dataclasses import dataclass


@dataclass
class Coord:

    x: float
    y: float

class Rectangle:

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





