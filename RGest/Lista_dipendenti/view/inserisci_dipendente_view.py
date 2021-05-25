from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox

from Dipendente.model.dipendente_model import dipendente_model
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller


class inserisci_dipendente_view(QMainWindow):

    def __init__(self, controller, callback):
        super(inserisci_dipendente_view, self).__init__()

        self.controller = controller
        self.callback = callback
        self.jsonobject = {}

        self.ldc = lista_dipendenti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.cognome = QLabel(self)
        self.nome = QLabel(self)
        self.eta = QLabel(self)
        self.postazione = QLabel(self)
        self.ruolo = QLabel(self)
        self.telefono = QLabel(self)
        self.stipendio = QLabel(self)
        self.completa = QLabel(self)

        self.ok = QPushButton(self)

        self.schermata()

    def schermata(self):

        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa,
                          "            Completa i seguenti campi",
                          100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, "Cognome", 180, 140, 200, 30, font)
        self.config_label(self.nome, "Nome", 180, 190, 200, 30, font)
        self.config_label(self.eta, "Eta", 180, 240, 200, 30, font)
        self.config_label(self.postazione, "Postazione", 180, 290, 200, 30, font)
        self.config_label(self.ruolo, "Ruolo", 180, 340, 200, 30, font)
        self.config_label(self.telefono, "Telefono", 180, 390, 200, 30, font)
        self.config_label(self.stipendio, "Stipendio[€]", 180, 440, 200, 30, font)

        self.Config_lineEdit("Cognome", 375, 140, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit("Nome", 375, 190, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit("Eta", 375, 240, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.config_comboBox("Postazione", 375, 290, ["Cucina", "Sala", "Backup"])
        self.config_comboBox("Ruolo", 375, 340, ["Chef", "Commis di cucina", "Lavapiatti", "Economo", "Maître", "Cameriere", "Sommelier", "Cassiere"])
        self.Config_lineEdit("Telefono", 375, 390, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit("Stipendio", 375, 440, "", False, QRegExpValidator(QRegExp("[0-9]+")))

        self.ok.setText("Conferma")
        self.ok.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.ok.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.ok.move(300, 520)
        self.ok.setFixedSize(150, 30)
        self.ok.clicked.connect(self.aggiunta_dipendente)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, tipo, a, b, text, flag, validatore):
        lineEdit = QLineEdit(self)
        lineEdit.setValidator(validatore)
        lineEdit.setPlaceholderText("Inserire i dati...")
        lineEdit.setText(text)
        lineEdit.setReadOnly(flag)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)
        self.jsonobject[tipo] = lineEdit

    def config_comboBox(self, tipo, a, b, lista):
        comboBox = QComboBox(self)
        comboBox.addItems(lista)
        comboBox.move(a, b)
        comboBox.setFont(QFont("Times Roman", 15))
        comboBox.setStyleSheet("background-color: rgb(255, 255, 255)")
        comboBox.setFixedSize(200, 30)
        self.jsonobject[tipo] = comboBox

    def aggiunta_dipendente(self):
        cognome = self.jsonobject["Cognome"].text()
        nome = self.jsonobject["Nome"].text()
        eta = self.jsonobject["Eta"].text()
        postazione = self.jsonobject["Postazione"].currentText()
        ruolo = self.jsonobject["Ruolo"].currentText()
        telefono = self.jsonobject["Telefono"].text()
        stipendio = self.jsonobject["Stipendio"].text()
        if(self.isBlank(cognome) or self.isBlank(nome) or self.isBlank(eta) or self.isBlank(telefono) or self.isBlank(stipendio)):
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        elif not self.controllo(postazione, ruolo):
            QMessageBox.critical(None, "RGest", "Postazione e ruolo non corrispondono!")
        elif int(eta) < 14:
            QMessageBox.critical(None, "RGest", "Lavoro minorile non ammesso!")
        elif int(eta) > 67:
            QMessageBox.critical(None, "RGest", "Il nuovo dipendente dovrebbe già essere in pensione! Impossibile aggiungere una persona con questa età!")
        else:
            self.controller.aggiungi_dipendente(dipendente_model(cognome, nome, ruolo, postazione, stipendio, telefono, eta))
            self.callback()
            QMessageBox.information(None, "RGest", "Dipendente inserito correttamente.")
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True

    def controllo(self, postazione, ruolo):
        cucina = ["Chef", "Commis di cucina", "Lavapiatti"]
        sala = ["Maître", "Cameriere", "Sommelier", "Cassiere"]
        backup = ["Economo"]
        if postazione == "Cucina" and not cucina.__contains__(ruolo):
            flag = False
        elif postazione == "Sala" and not sala.__contains__(ruolo):
            flag = False
        elif postazione == "Backup" and not backup.__contains__(ruolo):
            flag = False
        else:
            flag = True
        return flag