from PyQt6 import QtWidgets, uic
import sys

class OtherWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/form.ui', self)

    def setText(self, text):
        self.label.setText(text)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.otherwindows = OtherWindow()
        self.i = 0
        self.show()
        self.otherwindows.show()


    def pushButton_clicked(self):
        self.i += 1
        self.otherwindows.setText(f"Hello from Main Window {self.i}")



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


