import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog, QWidget
from ui.search_window import Ui_MainWindow
from ui.detail_window import Ui_Form
from PyQt6 import QtWidgets
import media
import config


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
        self.res = self.service.search_by_title(text.strip())
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

    def saveButton_clicked(self):
        print("Save")




app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
