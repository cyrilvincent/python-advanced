from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QCheckBox
import math
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.input = QLineEdit()
        self.checkbox = QCheckBox("Degrees")
        self.button = QPushButton("OK")
        self.button.clicked.connect(self.button_clicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def button_clicked(self):
        value = float(self.input.text())
        if self.checkbox.isChecked():
            value = math.radians(value)
        result = math.sin(value)
        self.label.setText(f"{result:.2f}")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()