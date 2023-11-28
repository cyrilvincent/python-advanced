from PyQt6 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/form.ui', self)
        self.show()
        self.textEdit.setText("Hello")
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.textEdit.setText("Clicked")



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


