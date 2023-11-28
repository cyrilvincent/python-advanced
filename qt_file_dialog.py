import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QApplication, QWidget


class filedialogdemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("QFileDialog")
        self.btn.clicked.connect(self.getfile)
        self.le = QLabel("Hello")
        self.contents = QTextEdit()
        self.setWindowTitle("File Dialog demo")

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.le)
        layout.addWidget(self.contents)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            './data', "Image files (*.jpg *.gif)")
        pixmap = QPixmap(fname[0])
        self.le.setPixmap(pixmap)



def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()