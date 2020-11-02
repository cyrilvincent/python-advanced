class Rectangle:

    def __init__(self, width:float=0, length:float=0):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

