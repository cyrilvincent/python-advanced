class Rectangle:

    def __init__(self, width:float=0, length:float=0):
        self._width = width
        self._length = length

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

