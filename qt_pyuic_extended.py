import sys

from PyQt6.QtWidgets import QMainWindow

from qt_pyuic import Ui_MainWindow
from PyQt6 import QtWidgets, uic

class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionCompute.triggered.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        self.result_label.setText("TOTO")

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
