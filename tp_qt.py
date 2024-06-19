import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog
from ui.search_window import Ui_MainWindow
from PyQt6 import QtWidgets
import media
import config


class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.service = media.BookService()
        self.service.load(config.csv_path)
        self.radioTitleButton.setChecked(True)
        self.show()

    def pushButton_clicked(self):
        text = self.lineEdit.text()
        res = self.service.search_by_title(text.strip())
        for book in res:
            self.listWidget.addItem(book.title)



app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()