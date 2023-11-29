import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog

from qt_pyuic import Ui_MainWindow
from PyQt6 import QtWidgets, uic
import house_service

class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionOpen.triggered.connect(self.fileOpen_trigerred)
        self.service = house_service.HouseService()
        self.show()

    def pushButton_clicked(self):
        print("Btn Ok")
        result = self.service.mean("surface")
        self.label.setText(f"{result}:.2f")

    def fileOpen_trigerred(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            './data')
        self.service.load(fname[0])
        print("Load Ok")

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
