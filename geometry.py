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

    def __repr__(self):
        return f"Rectangle {self.width}x{self.length}"

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


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

class TriangleRectangle(Rectangle):

    @property
    def area(self):
        return super(Rectangle).area / 2

    @property
    def hypothenuse(self):
        return (self.width ** 2 + self.length ** 2) ** 0.5

    @property
    def perimeter(self):
        return self.width + self.length + self.hypothenuse


if __name__ == '__main__':
    r = Rectangle(3,2)

