from PyQt6 import QtWidgets, uic
import media
import sys
import tp_house


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.service = tp_house.HouseService("data/house/house.csv")
        self.show()

    def pushButton_clicked(self):
        slope, intercept = self.service.lineregress()
        self.result_label.setText(f"{slope}, {intercept}")
        self.service.show()

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


