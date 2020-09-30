class Rectangle:

    def __init__(self, width=0, length=0):
        self._width = width
        self._length = length

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