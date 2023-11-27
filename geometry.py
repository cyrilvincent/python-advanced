from dataclasses import dataclass

@dataclass
class Point:

    x: float
    y: float


class Rectangle:

    def __init__(self, width: float, length: float, origin:Point=Point(0,0)):
        self._width = width
        self.length = length
        self.origin = origin

    def get_perimeter(self):
        return 2 * (self._width + self.length)

    def get_area(self):
        return self._width * self.length

    def move(self, x, y):
        self.origin.x = x
        self.origin.y = y

    @property
    def area(self):
        return self._width * self.length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def __del__(self):
        print("Bye bye")

    # Appelé quand
    # r = Rectangle(...)
    # r = None
    # del(r)
    # r = r2

@dataclass
class Rectangle2:

    length: float
    width: float

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    r = Rectangle(3,2)
