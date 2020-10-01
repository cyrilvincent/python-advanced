import config

if __name__ == '__main__':
    #opengl = OpenGL() Interdit
    openglinstance = config.driver
    openglinstance.drawPoint(0, 0)
    openglinstance.drawLine(0, 0, 1, 1)