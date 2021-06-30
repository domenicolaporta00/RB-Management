from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox

from Lista_tasse.controller.lista_tasse_controller import lista_tasse_controller
from Tasse.model.tasse_model import tasse_model


class tasse_view(QMainWindow):

    def __init__(self, controller):
        super(tasse_view, self).__init__()

        self.controller = controller
        # self.callback = callback
        self.jsonobject = {}

        self.ltc = lista_tasse_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.acqua = QLabel(self)
        self.luce = QLabel(self)
        self.gas = QLabel(self)
        self.tv = QLabel(self)
        self.affitto = QLabel(self)

        self.confermaButton = QPushButton(self)

        self.completa = QLabel(self)

        self.schermata()

    def schermata(self):
        validator = QRegExpValidator(QRegExp("[0-9]+"))
        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa, "Completa i seguenti campi",
                          200, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))
        self.config_label(self.acqua, "Acqua", 210, 140, 190, 30, font)
        self.config_label(self.luce, "Luce", 210, 220, 190, 30, font)
        self.config_label(self.gas, "Gas", 210, 300, 190, 30, font)
        self.config_label(self.tv, "Tv", 210, 380, 190, 30, font)
        self.config_label(self.affitto, "Affitto", 210, 460, 190, 30, font)

        self.Config_lineEdit("Acqua", 345, 140, "", validator)
        self.Config_lineEdit("Luce", 345, 220, "", validator)
        self.Config_lineEdit("Gas", 345, 300, "", validator)
        self.Config_lineEdit("Tv", 345, 380, "", validator)
        self.Config_lineEdit("Affitto", 345, 460, "", validator)

        self.config_button("Conferma", 300, 540, self.confermaButton)
        self.confermaButton.clicked.connect(self.conferma)

    def config_button(self, text, x, y, bottone):
        bottone.setText(text)
        bottone.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        bottone.setFont(QFont("Times Roman", 11, QFont.Bold))
        bottone.move(x, y)
        bottone.setFixedSize(150, 30)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, tipo, a, b, text, val):
        lineEdit = QLineEdit(self)
        lineEdit.setPlaceholderText("Importo...[€]")
        lineEdit.setText(text)
        lineEdit.setValidator(val)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)
        self.jsonobject[tipo] = lineEdit

    def conferma(self):
        acqua = self.jsonobject["Acqua"].text()
        luce = self.jsonobject["Luce"].text()
        gas = self.jsonobject["Gas"].text()
        tv = self.jsonobject["Tv"].text()
        affitto = self.jsonobject["Affitto"].text()
        if self.isBlank(acqua) or self.isBlank(luce) or self.isBlank(
                gas) or self.isBlank(tv) or self.isBlank(affitto):
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        else:
            self.controller.aggiungi_tasse(tasse_model(acqua, luce, gas, tv, affitto))
            # self.callback()
            QMessageBox.information(None, "RGest", "Tasse inserite correttamente.")
            self.controller.save_data()
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True
