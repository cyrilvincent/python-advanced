class Rectangle:

    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length
