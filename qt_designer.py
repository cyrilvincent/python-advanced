from PyQt6 import QtWidgets, uic
import media
import sys
import tp_house


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        self.result_label.setText(f"hello")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()



