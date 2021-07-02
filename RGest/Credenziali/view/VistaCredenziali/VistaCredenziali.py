from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QMessageBox, QFrame, QInputDialog

from Credenziali.controller.ControllerCredenziali import ControllerCredenziali
from Credenziali.view.VistaCredenziali.VistaCambioCredenziali import VistaCambioCredenziali
from Schermata_principale.view.Schermata_principale_view import Schermata_principale_view


class VistaCredenziali(QMainWindow):
    def __init__(self, lingua):
        super(VistaCredenziali, self).__init__()

        self.lingua = lingua

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

        # self.vcc = VistaCambioCredenziali()
        self.controller_credenziali = ControllerCredenziali()
        # self.spv = Schermata_principale_view()

        self.schermata()

    def schermata(self):
        print(1)
        global str1, str2, str8, str9
        print(2)
        font = QFont("Times Roman", 11)
        f = QFont("Times Roman", 11, QFont.Bold)
        pixmax = QPixmap("images\\Logo_splash.png")

        if self.lingua == "Inglese":
            str1 = "Welcome!"
            str2 = "Username"
            str8 = "Login"
            str9 = "Change credentials"
        elif self.lingua == "Italiano":
            str1 = "Benvenuto!"
            str2 = "Nome utente"
            str8 = "Accedi"
            str9 = "Cambio credenziali"
        self.logo.setPixmap(pixmax)
        self.logo.move(240, 300)
        self.logo.setFixedSize(300, 300)

        self.config_label(self.benvenuto, str1, 240, 0, 300, 200, QFont("Times Roman", 40, QFont.Bold))

        self.config_label(self.testoNome, str2, 250, 150, 100, 30, f)

        self.config_label(self.testoPassword, "Password", 250, 200, 100, 30, f)

        self.insertNome.move(375, 150)
        self.insertNome.setFixedSize(150, 30)
        self.insertNome.setFont(font)

        self.insertPassword.setEchoMode(QLineEdit.Password)
        self.insertPassword.move(375, 200)
        self.insertPassword.setFixedSize(150, 30)
        self.insertPassword.setFont(font)

        self.config_button(self.accedi, str8, QFont("Times Roman", 11, QFont.Bold), 100, 30, 250, 250)
        self.accedi.clicked.connect(self.controllo)

        self.config_button(self.cc, str9, QFont("Times Roman", 11, QFont.Bold), 150, 30, 375, 250)
        self.cc.clicked.connect(self.cambioCredenziali)

    def controllo(self):
        global str3, str4, str5, str6, str7
        if self.lingua == "Inglese":
            str3 = "Signed in successfully"
            str4 = "What's your name?"
            str5 = "Type something"
            str6 = "Fill in all fields"
            str7 = "Incorrect login data"
        elif self.lingua == "Italiano":
            str3 = "Accesso effettuato correttamente"
            str4 = "Come ti chiami?"
            str5 = "Digitare qualcosa!"
            str6 = "Compilare tutti i campi!"
            str7 = "Dati di accesso errati!"
        if self.controller_credenziali.controllaCredenziali(self.insertNome.text(), self.insertPassword.text()):
            QMessageBox.information(None, "RGest", str3)
            self.close()
            # self.spv.show()
            text, select = QInputDialog.getText(None, "RGest", str4)
            if not select:
                pass
            else:
                if not text:
                    QMessageBox.warning(None, "RGest", str5)
                else:
                    self.nome = text
            self.spv = Schermata_principale_view(self.nome, self.lingua)
            self.spv.show()
        elif self.insertNome.text().isspace() or self.insertPassword.text().isspace():
            QMessageBox.warning(None, "RGest", str6)
        elif self.insertNome.text() == "" or self.insertPassword.text() == "":
            QMessageBox.warning(None, "RGest", str6)
        else:
            QMessageBox.critical(None, "RGest", str7)

    def cambioCredenziali(self):
        self.vcc = VistaCambioCredenziali(self.lingua)
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