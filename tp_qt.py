# Qt avec un lineEdit + Button + label
# Saisir un chiffre dans lineEdit
# Quand on appuie sur le button affiche le sin dans le label : float() math.sin(radian)
# Bonus : Gérer les exceptions : try except : 2ème label : affiche l'erreur
# Bonus : QCheckBox if checked => radians sinon en degres : math.radians()
# Reprise à 16h05

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QCheckBox
import math
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tp")
        self.input = QLineEdit()
        self.button = QPushButton("Calculate")
        self.label = QLabel()
        self.label_error = QLabel("ERROR")
        self.label_error.setVisible(False)
        self.checkbox = QCheckBox("Degrees")
        self.checkbox.stateChanged.connect(self.button_clicked)
        self.button.clicked.connect(self.button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.label_error)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def button_clicked(self):
        self.label_error.setVisible(False)
        try:
            value = float(self.input.text())
            if self.checkbox.isChecked():
                value = math.radians(value)
            res = math.sin(value)
            self.label.setText(f"{res:.5f}")
        except ValueError as ex:
            self.label_error.setText(f"Error: {ex}")
            self.label_error.setVisible(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
