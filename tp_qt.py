import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog, QWidget
from ui.search_window import Ui_MainWindow
from ui.detail_window import Ui_Form
from PyQt6 import QtWidgets
import media
import config
import re


class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.listWidget.currentItemChanged.connect(self.listWidget_currentItemChanged)
        self.service = media.BookService()
        self.service.load(config.csv_path)
        self.radioTitleButton.setChecked(True)
        self.res = []
        self.detail_window = None
        self.show()

    def pushButton_clicked(self):
        text = self.lineEdit.text()
        if self.radioTitleButton.isChecked():
            self.res = self.service.search_by_title(text.strip())
        elif self.radioPriceButton.isChecked():
            self.res = self.service.search_by_price(float(text.strip()))
        else:
            self.res = [self.service.search_by_ean(text.strip())]
        self.listWidget.clear()
        for book in self.res:
            self.listWidget.addItem(book.title)

    def listWidget_currentItemChanged(self):
        book = self.res[self.listWidget.currentRow()]
        self.detail_window = DetailWindow(book)
        self.detail_window.show()
        print("OK")



class DetailWindow(QWidget, Ui_Form):

    def __init__(self, book: media.Book):
        super().__init__()
        self.setupUi(self)
        self.book = book
        self.pushButton.clicked.connect(self.saveButton_clicked)
        self.idLineEdit.setText(book.ean)
        self.titleLineEdit.setText(book.title)
        self.priceLineEdit.setText(f"{book.net_price():.2f} €")
        self.regex = r"^\d{3}-\d-\d{2}-\d{6}-\d$"

    def saveButton_clicked(self):
        print(re.match(self.regex, self.idLineEdit.text()) is not None)




app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
