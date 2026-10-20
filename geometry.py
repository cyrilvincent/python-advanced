class Rectangle:
    """
    Docstring for Rectangle
    """

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """
        Compute area
        
        :param self: Description
        """
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.length + self.width)