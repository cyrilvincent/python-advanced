from PyQt6 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/form.ui', self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


