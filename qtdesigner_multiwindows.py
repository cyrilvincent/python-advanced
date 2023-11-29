from PyQt6 import QtWidgets, uic
import media
import sys
class OtherWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui/form.ui', self)

    def setText(self, text):
        self.label.setText(text)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.service = media.MediaService()
        self.service.load("data/media/books.csv")
        self.otherwindows = OtherWindow()
        self.otherwindows.setText("Hello from Main Window")
        self.show()

    def pushButton_clicked(self):
        self.otherwindows.show()



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


