from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox

from Dipendente.model.dipendente_model import dipendente_model
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller


class inserisci_dipendente_view(QMainWindow):

    def __init__(self, controller, callback, lingua):
        super(inserisci_dipendente_view, self).__init__()

        self.lingua = lingua

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

        global str1, str8, str7, str6, str5, str4, str3, str2, str9, str11, str12, str13, str14, str15, str16, str10
        if self.lingua == "Inglese":
            str1 = "        Complete the following fields"
            str2 = "Surname"
            str3 = "Name"
            str4 = "Age"
            str5 = "Station"
            str6 = "Role"
            str7 = "Telephone"
            str8 = "Salary[€]"
            str9 = "Kitchen"
            str10 = "Hall"
            str11 = "Kitchen commis"
            str12 = "Dishwasher"
            str13 = "Treasurer"
            str14 = "Waiter"
            str15 = "Cashier"
            str16 = "Confirm"
        if self.lingua == "Italiano":
            str1 = "            Completa i seguenti campi"
            str2 = "Cognome"
            str3 = "Nome"
            str4 = "Età"
            str5 = "Postazione"
            str6 = "Ruolo"
            str7 = "Telefono"
            str8 = "Stipendio[€]"
            str9 = "Cucina"
            str10 = "Sala"
            str11 = "Commis di cucina"
            str12 = "Lavapiatti"
            str13 = "Economo"
            str14 = "Cameriere"
            str15 = "Cassiere"
            str16 = "Conferma"

        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa, str1, 100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, str2, 180, 140, 200, 30, font)
        self.config_label(self.nome, str3, 180, 190, 200, 30, font)
        self.config_label(self.eta, str4, 180, 240, 200, 30, font)
        self.config_label(self.postazione, str5, 180, 290, 200, 30, font)
        self.config_label(self.ruolo, str6, 180, 340, 200, 30, font)
        self.config_label(self.telefono, str7, 180, 390, 200, 30, font)
        self.config_label(self.stipendio, str8, 180, 440, 200, 30, font)

        self.Config_lineEdit("Cognome", 375, 140, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit("Nome", 375, 190, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit("Eta", 375, 240, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.config_comboBox("Postazione", 375, 290, [str9, str10, "Backup"])
        self.config_comboBox("Ruolo", 375, 340,
                             ["Chef", str11, str12, str13, "Maître", str14, "Sommelier",
                              str15])
        self.Config_lineEdit("Telefono", 375, 390, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit("Stipendio", 375, 440, "", False, QRegExpValidator(QRegExp("[0-9]+")))

        self.ok.setText(str16)
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

        global str17
        if self.lingua == "Inglese":
            str17 = "Enter data..."
        if self.lingua == "Italiano":
            str17 = "Inserire i dati..."

        lineEdit = QLineEdit(self)
        lineEdit.setValidator(validatore)
        lineEdit.setPlaceholderText(str17)
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

        global str18, str19, str20, str21, str22
        if self.lingua == "Inglese":
            str18 = "Fill in all fields!"
            str19 = "Location and role do not match!"
            str20 = "Child labor not allowed!"
            str21 = "The new employee should already be retired! Impossible to add a person with this age!"
            str22 = "Employee entered correctly."
        if self.lingua == "Italiano":
            str18 = "Compilare tutti i campi!"
            str19 = "Postazione e ruolo non corrispondono!"
            str20 = "Lavoro minorile non ammesso!"
            str21 = "Il nuovo dipendente dovrebbe già essere in pensione! Impossibile aggiungere una persona con " \
                    "questa età! "
            str22 = "Dipendente inserito correttamente."

        cognome = self.jsonobject["Cognome"].text()
        nome = self.jsonobject["Nome"].text()
        eta = self.jsonobject["Eta"].text()
        postazione = self.jsonobject["Postazione"].currentText()
        ruolo = self.jsonobject["Ruolo"].currentText()
        telefono = self.jsonobject["Telefono"].text()
        stipendio = self.jsonobject["Stipendio"].text()
        if self.isBlank(cognome) or self.isBlank(nome) or self.isBlank(eta) or self.isBlank(telefono) or self.isBlank(
                stipendio):
            QMessageBox.warning(None, "RGest", str18)
        elif not self.controllo(postazione, ruolo):
            QMessageBox.critical(None, "RGest", str19)
        elif int(eta) < 14:
            QMessageBox.critical(None, "RGest", str20)
        elif int(eta) > 67:
            QMessageBox.critical(None, "RGest", str21)
        else:
            self.controller.aggiungi_dipendente(
                dipendente_model(cognome, nome, ruolo, postazione, stipendio, telefono, eta))
            self.callback()
            QMessageBox.information(None, "RGest", str22)
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True

    def controllo(self, postazione, ruolo):

        global str23, str24, str26, str27, str25, str28, str29
        if self.lingua == "Inglese":
            str23 = "Kitchen commis"
            str24 = "Dishwasher"
            str25 = "Treasurer"
            str26 = "Waiter"
            str27 = "Cashier"
            str28 = "Kitchen"
            str29 = "Hall"
        if self.lingua == "Italiano":
            str23 = "Commis di cucina"
            str24 = "Lavapiatti"
            str25 = "Economo"
            str26 = "Cameriere"
            str27 = "Cassiere"
            str28 = "Cucina"
            str29 = "Sala"

        cucina = ["Chef", str23, str24]
        sala = ["Maître", str26, "Sommelier", str27]
        backup = [str25]
        if postazione == str28 and not cucina.__contains__(ruolo):
            flag = False
        elif postazione == str29 and not sala.__contains__(ruolo):
            flag = False
        elif postazione == "Backup" and not backup.__contains__(ruolo):
            flag = False
        else:
            flag = True
        return flag
