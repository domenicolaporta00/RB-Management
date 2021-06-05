from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QMessageBox, QFrame

from Credenziali.controller.ControllerCredenziali import ControllerCredenziali
from Credenziali.view.VistaCredenziali.VistaCambioCredenziali import VistaCambioCredenziali
from Schermata_principale.view.Schermata_principale_view import Schermata_principale_view


class VistaCredenziali(QMainWindow):
    def __init__(self):
        super(VistaCredenziali, self).__init__()

        self.icona = QIcon("images\\Logo_splash.png")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        #self.setStyleSheet("background-color: rgb(0, 255, 255)")

        self.testoNome = QLabel(self)
        self.testoPassword = QLabel(self)
        self.benvenuto = QLabel(self)
        self.logo = QLabel(self)

        self.insertNome = QLineEdit(self)
        self.insertPassword = QLineEdit(self)

        self.accedi = QPushButton(self)
        self.cc = QPushButton(self)

        self.vcc = VistaCambioCredenziali()
        self.controller_credenziali = ControllerCredenziali()
        self.spv = Schermata_principale_view()

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11)
        f = QFont("Times Roman", 11, QFont.Bold)
        pixmax = QPixmap("images\\Logo_splash.png")

        self.logo.setPixmap(pixmax)
        self.logo.move(240, 300)
        self.logo.setFixedSize(300, 300)

        self.config_label(self.benvenuto, "Benvenuto!", 240, 0, 300, 200, QFont("Times Roman", 40, QFont.Bold))

        self.config_label(self.testoNome, "Nome Utente", 250, 150, 100, 30, f)

        self.config_label(self.testoPassword, "Password", 250, 200, 100, 30, f)

        self.insertNome.move(375, 150)
        self.insertNome.setFixedSize(150, 30)
        self.insertNome.setFont(font)

        self.insertPassword.setEchoMode(QLineEdit.Password)
        self.insertPassword.move(375, 200)
        self.insertPassword.setFixedSize(150, 30)
        self.insertPassword.setFont(font)

        '''self.accedi.move(250, 250)
        self.accedi.setText("Accedi")
        self.accedi.setFont(font)'''
        self.config_button(self.accedi, "Accedi", QFont("Times Roman", 11, QFont.Bold), 100, 30, 250, 250)
        self.accedi.clicked.connect(self.controllo)

        '''self.cc.move(375, 250)
        self.cc.setText("Cambia credenziali")
        self.cc.setFont(font)
        self.cc.setFixedSize(150, 30)'''
        self.config_button(self.cc, "Cambia credenziali", QFont("Times Roman", 11, QFont.Bold), 150, 30, 375, 250)
        self.cc.clicked.connect(self.cambioCredenziali)

    def controllo(self):
        if self.controller_credenziali.controllaCredenziali(self.insertNome.text(), self.insertPassword.text()):
            QMessageBox.information(None, "RGest", "Accesso effettuato correttamente.")
            self.spv.show()
            self.close()
        elif self.insertNome.text().isspace() or self.insertPassword.text().isspace():
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        elif self.insertNome.text() == "" or self.insertPassword.text() == "":
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        else:
            QMessageBox.critical(None, "RGest", "Dati di accesso errati!")

    def cambioCredenziali(self):
        self.vcc.show()
        self.close()

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)