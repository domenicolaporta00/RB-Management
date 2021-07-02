from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog

from Credenziali.controller.ControllerCredenziali import ControllerCredenziali
from Schermata_principale.view.Schermata_principale_view import Schermata_principale_view


class VistaCambioCredenziali(QMainWindow):
    def __init__(self, lingua):
        super(VistaCambioCredenziali, self).__init__()

        self.lingua = lingua

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        #self.setStyleSheet("background-color: rgb(0, 255, 255)")

        self.vecchia_password = QLabel(self)
        self.nuovo_nome_utente = QLabel(self)
        self.nuova_password = QLabel(self)
        self.conferma_password = QLabel(self)
        self.inserisci = QLabel(self)
        self.logo = QLabel(self)

        self.vPText = QLineEdit(self)
        self.nNUText = QLineEdit(self)
        self.nPText = QLineEdit(self)
        self.cPText = QLineEdit(self)

        self.confermaButton = QPushButton(self)

        self.controller_credenziali = ControllerCredenziali()
        # self.spv = Schermata_principale_view()

        self.schermata()

    def schermata(self):
        global str2, str7, str6, str5, str4, str3
        font = QFont("Times Roman", 11, QFont.Bold)
        f = QFont("Times Roman", 20, QFont.Bold)
        pixmax = QPixmap("images\\Logo_splash.png")

        if self.lingua == "Inglese":
            str2 = "Confirm"
            str3 = "Enter the new credentials"
            str4 = "Old password"
            str5 = "New username"
            str6 = "New Password"
            str7 = "Confirm password"
        elif self.lingua == "Italiano":
            str2 = "Conferma"
            str3 = "Inserisci le nuove credenziali"
            str4 = "Vecchia password"
            str5 = "Nuovo nome utente"
            str6 = "Nuova password"
            str7 = "Conferma password"

        self.logo.setPixmap(pixmax)
        self.logo.move(230, 330)
        self.logo.setFixedSize(300, 300)

        self.config_label(self.inserisci, str3, 175, -60, 400, 200, f)

        self.config_label(self.vecchia_password, str4, 220, 90, 150, 30, font)

        self.config_label(self.nuovo_nome_utente, str5, 220, 140, 150, 30, font)

        self.config_label(self.nuova_password, str6, 220, 190, 150, 30, font)

        self.config_label(self.conferma_password, str7, 220, 240, 150, 30, font)

        self.vPText.setEchoMode(QLineEdit.Password)
        self.vPText.setFixedSize(150, 30)
        self.vPText.move(385, 90)
        self.vPText.setFont(font)

        self.nNUText.move(385, 140)
        self.nNUText.setFixedSize(150, 30)
        self.nNUText.setFont(QFont("Times Roman", 11))

        self.nPText.move(385, 190)
        self.nPText.setFixedSize(150, 30)
        self.nPText.setEchoMode(QLineEdit.Password)
        self.nPText.setFont(font)

        self.cPText.move(385, 240)
        self.cPText.setEchoMode(QLineEdit.Password)
        self.cPText.setFixedSize(150, 30)
        self.cPText.setFont(font)

        self.config_button(self.confermaButton, str2, QFont("Times Roman", 11, QFont.Bold), 150, 30, 300, 290)
        self.confermaButton.clicked.connect(self.aggiornamentoCredenziali)

    def aggiornamentoCredenziali(self):
        global str7, str6, str5, str4, str3, str2
        if self.lingua == "Inglese":
            str2 = "Fill in all fields"
            str3 = "Confirm different password! Credentials not changed!"
            str4 = "Credentials changed successfully."
            str5 = "What's your name?"
            str6 = "Type something"
            str7 = "Wrong old password! Credentials not changed!"
        elif self.lingua == "Italiano":
            str2 = "Compilare tutti i campi!"
            str3 = "Conferma password diversa! Credenziali non modificate!"
            str4 = "Credenziali modificate correttamente"
            str5 = "Come ti chiami?"
            str6 = "Digitare qualcosa!"
            str7 = "Vecchia password errata! Credenziali non modificate!"

        if self.nPText.text().isspace() or self.nNUText.text().isspace() or self.vPText.text().isspace() or self.cPText.text().isspace():
            QMessageBox.warning(None, "RGest", str2)

        elif self.nPText.text() == "" or self.nNUText.text() == "" or self.vPText.text() == "" or self.cPText.text() == "":
            QMessageBox.warning(None, "RGest", str2)

        elif self.nPText.text() != self.cPText.text():
            QMessageBox.critical(None, "RGest", str3)

        elif self.controller_credenziali.controlloPassword(self.vPText.text()):
            self.controller_credenziali.aggiornaCredenziali(self.nNUText.text(), self.nPText.text())
            QMessageBox.information(None, "RGest", str4)
            self.close()
            text, select = QInputDialog.getText(None, "RGest", str5)
            if not select:
                pass
            else:
                if not text:
                    QMessageBox.warning(None, "RGest", str6)
                else:
                    self.nome = text
            self.spv = Schermata_principale_view(self.nome, self.lingua)
            self.spv.show()

        elif not self.controller_credenziali.controlloPassword(self.nPText.text()):
            QMessageBox.critical(None, "RGest", str7)

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