import sys

from PyQt6.QtWidgets import QMainWindow, QFileDialog
from ui.main import Ui_MainWindow
from PyQt6 import QtWidgets
import media


class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionOpen.triggered.connect(self.fileOpen_trigerred)
        self.service = media.MediaService()
        self.show()

    def pushButton_clicked(self):
        title = self.lineEdit.text()
        l = self.service.get_book_by_title(title)
        if len(l) == 0:
            self.result_label.setText("Aucun")
        else:
            self.result_label.setText(l[0].title)

    def fileOpen_trigerred(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            './data/media')
        self.service.load(fname[0])

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
