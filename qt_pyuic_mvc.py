import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog
from ui.main import Ui_MainWindow
from PyQt6 import QtWidgets


class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionOpen.triggered.connect(self.fileOpen_trigerred)
        self.show()

    def pushButton_clicked(self):
        print("Btn Ok")

    def fileOpen_trigerred(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            './data')
        print("Load Ok")

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
