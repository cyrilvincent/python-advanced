from dataclasses import dataclass


@dataclass
class Point:

    x: float
    y: float

    def move(self, x: float, y: float):
        self.x = x
        self.y = y

    def relative(self, x: float, y: float):
        self.x += x
        self.y += y

    

class Rectangle:
    """
    Docstring for Rectangle
    """

    def __init__(self, length: float, width: float, origin: Point):
        self.length = length
        self.width = width
        self.origin = origin

    def area(self):
        """
        Compute area
        
        :param self: Description
        """
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class RectangleCollection:

    def __init__(self, items: list[Rectangle] = []):
        self.items = items
    
    def areas(self):
        return sum([r.area() for r in self.items])
    
class Square(Rectangle):

    def __init__(self, side: float, origin):
        super().__init__(side, side, origin)
        