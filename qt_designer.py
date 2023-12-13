from PyQt6 import QtWidgets, uic
import media
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        self.result_label.setText("Pushed")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()

# TP
# Créer dans qtdesigner une fenêtre avec linedit + checkbox + button + label  + errorlabel (rouge)
# Sauvegarder dans ui/main.ui
# Créer votre class MainWindow
# Charger l'ui avec uic.loadUi('ui/main.ui', self)
# Faire slot qui affiche un message dans le label
# Bonus : Créer un menu File + Open + Compute et un menu About + About
# Pour un élément du menu le signal = trigerred
# Quand on choisit compute ca affiche compute dans le label


