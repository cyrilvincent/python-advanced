#OpenGL = norme
#NVidia = implémentation OpenGL = Driver OpenGL
#Intel = implémentation OpenGL = Driver Intel
import abc

class OpenGL(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drawPoint(self, x, y):...

    @abc.abstractmethod
    def drawLine(self, x1, y1, x2, y2):...

class NVidiaOpenGLDriver(OpenGL):

    def __init__(self, name = "NVidia"):
        self.name = name

    def drawPoint(self, x, y):
        print(f"NVidia:({x},{y})")

    def drawLine(self, x1, y1, x2, y2):
        print(f"NVidia:({x1},{y1})-({x2},{y2})")

class IntelOpenGLDriver(OpenGL):

    def __init__(self, name = "Intel"):
        self.name = name

    def drawPoint(self, x, y):
        print(f"Intel:({x},{y})")

    def drawLine(self, x1, y1, x2, y2):
        print(f"Intel:({x1},{y1})-({x2},{y2})")



