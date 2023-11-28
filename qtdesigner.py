from PyQt6 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        self.result_label.setText("TOTO")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


