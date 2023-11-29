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
        # if self.checkbox.ischecked():
        #     res = self.service.get_by_price(10)
        # else:
        #     res = self.service.get_by_title("Python")
        res = self.service.get_by_price(10)
        self.result_label.setText(f"{res[0].title} {res[0].price:.2f}€")



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


