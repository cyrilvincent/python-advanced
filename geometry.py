from dataclasses import dataclass


class Rectangle:

    def __init__(self, width: float, length: float):
        self._width = width
        self.length = length

    def get_perimeter(self):
        return 2 * (self._width + self.length)

    def get_area(self):
        return self._width * self.length

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
