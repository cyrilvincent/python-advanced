class Rectangle:

    def __init__(self, length=0, width=0):
        self._length = length
        self.width = width
        
    @property
    def length(self):
        return self.length

    @length.setter
    def length(self, value):
        pass

    @property
    def area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def scale(self, scale):
        self.width *= scale
        self.length *= scale
