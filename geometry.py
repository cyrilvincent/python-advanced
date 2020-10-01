class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:

    toto = 3

    def __init__(self, width=0, length=0, origin:Point = Point()):
        self._width = width
        self._length = length
        self.origin = origin


    def perimeter(self):
        return 2 * (self._width + self._length)

    def area(self):
        return self._width * self._length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError
        else:
            self._width = value

    def move(self, x, y):
        self.origin.x = x
        self.origin.y = y