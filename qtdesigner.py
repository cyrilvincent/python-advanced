from PyQt6 import QtWidgets, uic
import media
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.service = media.MediaService()
        self.service.load("data/media/books.csv")
        self.show()

    def pushButton_clicked(self):
        res = self.service.get_by_price(10)
        self.result_label.setText(res[0].title)



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


