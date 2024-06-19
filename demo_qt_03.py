import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.button_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Clicked")
        self.button.setText("Clicked")
        self.button.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()