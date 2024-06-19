import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog
from ui.main import Ui_MainWindow
from PyQt6 import QtWidgets


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.mainWindow.pushButton.clicked.connect(self.pushButton_clicked)
        self.mainWindow.actionOpen.triggered.connect(self.fileOpen_trigerred)
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
