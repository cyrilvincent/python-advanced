import sys

from demo_pyuic import Ui_MainWindow
from PyQt6 import QtWidgets, uic

class MyApp(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        super().setupUi(Ui_MainWindow)

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
