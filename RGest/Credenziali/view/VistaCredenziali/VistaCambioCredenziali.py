from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame

from Credenziali.controller.ControllerCredenziali import ControllerCredenziali
from Schermata_principale.view.Schermata_principale_view import Schermata_principale_view


class VistaCambioCredenziali(QMainWindow):
    def __init__(self):
        super(VistaCambioCredenziali, self).__init__()

        self.icona = QIcon("C:\\Users\\DELL\\Desktop\\Progetto Ingegneria del Software\\Logo_definitivo.jpg")

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
        self.spv = Schermata_principale_view()

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11)
        f = QFont("Times Roman", 20)
        pixmax = QPixmap("C:\\Users\\DELL\\Desktop\\Progetto Ingegneria del Software\\Logo_definitivo.jpg")

        self.logo.setPixmap(pixmax)
        self.logo.move(230, 330)
        self.logo.setFixedSize(300, 300)

        self.inserisci.setText("Inserisci le nuove credenziali")
        self.inserisci.setFont(f)
        self.inserisci.move(210, -60)
        self.inserisci.setFixedSize(350, 200)

        self.vecchia_password.setText("Vecchia password")
        self.vecchia_password.setFont(font)
        self.vecchia_password.move(220, 90)
        self.vecchia_password.setFixedSize(150, 30)
        self.vecchia_password.setFrameShape(QFrame.Panel)
        self.vecchia_password.setFrameShadow(QFrame.Sunken)

        self.nuovo_nome_utente.setText("Nuovo nome utente")
        self.nuovo_nome_utente.setFont(font)
        self.nuovo_nome_utente.move(220, 140)
        self.nuovo_nome_utente.setFixedSize(150, 30)
        self.nuovo_nome_utente.setFrameShape(QFrame.Panel)
        self.nuovo_nome_utente.setFrameShadow(QFrame.Sunken)

        self.nuova_password.setText("Nuova password")
        self.nuova_password.setFont(font)
        self.nuova_password.move(220, 190)
        self.nuova_password.setFixedSize(150, 30)
        self.nuova_password.setFrameShape(QFrame.Panel)
        self.nuova_password.setFrameShadow(QFrame.Sunken)

        self.conferma_password.setText("Conferma password")
        self.conferma_password.setFont(font)
        self.conferma_password.move(220, 240)
        self.conferma_password.setFixedSize(150, 30)
        self.conferma_password.setFrameShape(QFrame.Panel)
        self.conferma_password.setFrameShadow(QFrame.Sunken)

        self.vPText.setEchoMode(QLineEdit.Password)
        self.vPText.setFixedSize(150, 30)
        self.vPText.move(385, 90)
        self.vPText.setFont(font)

        self.nNUText.move(385, 140)
        self.nNUText.setFixedSize(150, 30)
        self.nNUText.setFont(font)

        self.nPText.move(385, 190)
        self.nPText.setFixedSize(150, 30)
        self.nPText.setEchoMode(QLineEdit.Password)
        self.nPText.setFont(font)

        self.cPText.move(385, 240)
        self.cPText.setEchoMode(QLineEdit.Password)
        self.cPText.setFixedSize(150, 30)
        self.cPText.setFont(font)

        self.confermaButton.setText("Conferma")
        self.confermaButton.move(325, 290)
        self.confermaButton.setFont(font)
        self.confermaButton.clicked.connect(self.aggiornamentoCredenziali)

    def aggiornamentoCredenziali(self):

        if self.nPText.text().isspace() or self.nNUText.text().isspace() or self.vPText.text().isspace() or self.cPText.text().isspace():
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")

        elif self.nPText.text() == "" or self.nNUText.text() == "" or self.vPText.text() == "" or self.cPText.text() == "":
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")

        elif self.nPText.text() != self.cPText.text():
            QMessageBox.critical(None, "RGest", "Conferma password diversa! Credenziali non modificate!")

        elif self.controller_credenziali.controlloPassword(self.vPText.text()):
            self.controller_credenziali.aggiornaCredenziali(self.nNUText.text(), self.nPText.text())
            QMessageBox.information(None, "RGest", "Credenziali modificate correttamente.")
            self.close()
            self.spv.show()

        elif not self.controller_credenziali.controlloPassword(self.nPText.text()):
            QMessageBox.critical(None, "RGest", "Vecchia password errata! Credenziali non modificate!")