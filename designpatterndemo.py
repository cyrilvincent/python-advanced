# VideoGame -- OpenGL(API)
#               |       |
#             NVidia   Intel

import abc

class OpenGL(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drawpoint(self, x, y):...

    @abc.abstractmethod
    def drawline(self, x1, y1, x2, y2):...

class NVidiaDriver(OpenGL):

    def drawpoint(self, x, y):
        print(f"({x},{y})")

    def drawline(self, x1, y1, x2, y2):
        print("Line")

class IntelDriver(OpenGL):

    def drawpoint(self, x, y):
        print(f"{x}-{y}")

    def drawline(self, x1, y1, x2, y2):
        print(f"LineIntel")

class VideoGame:

    def __init__(self, driver:OpenGL):
        self.driver:OpenGL = driver

    def play(self):
        self.driver.drawpoint(3,2)

if __name__ == '__main__':
    game = VideoGame(IntelDriver())
    game.play()