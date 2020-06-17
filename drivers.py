# OpenGL

import abc
class OpenGLPattern(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, id):...

    @abc.abstractmethod
    def plotPoint(self, x, y):...

    @abc.abstractmethod
    def drawLine(self, x1,y1, x2, y2):...

class OpenGLNVidia(OpenGLPattern):

    def __init__(self, id):
        self.id = id

    def plotPoint(self, x, y):
        return f"({x},{y})"

    def drawLine(self, x1, y1, x2, y2):
        pass

class OpenGLIntel(OpenGLPattern):

    def __init__(self, id):
        self.id = id

    def plotPoint(self, x, y):
        return f"[{x},{y}]"

    def drawLine(self, x1, y1, x2, y2):
        pass

class VideoGame:

    def __init__(self, driver):
        self.driver = driver

    def display2Points(self, x1,y1, x2, y2):
        self.driver.plotPoints(x1,y1)
        self.driver.plotPoints(x2, y2)

if __name__ == '__main__':
    #driver = OpenGLNVidia(1)
    driver = OpenGLIntel(2)
    vg = VideoGame(driver)
    vg.display2Points(2,3,4,5)


