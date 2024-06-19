import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QListWidget, QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.list = QListWidget()
        for i in range(5):
            self.list.addItem(f"Item {i}")
        self.list.currentItemChanged.connect(self.item_changed)

        self.setCentralWidget(self.list)

    def item_changed(self):
        print(self.list.currentItem(), self.list.currentRow())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()