from PyQt5.QtCore import QRegExp, QTime
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QTimeEdit, QMessageBox

from Delivery.model.delivery_model import delivery_model
from Lista_delivery.controller.lista_delivery_controller import lista_delivery_controller


class inserisci_delivery_view(QMainWindow):

    def __init__(self, controller, callback, cb_cena, lingua):
        super(inserisci_delivery_view, self).__init__()

        self.lingua = lingua

        self.controller = controller
        self.callback = callback
        self.cb_cena = cb_cena
        self.jsonobject = {}

        self.ldc = lista_delivery_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.cognome = QLabel(self)
        self.orario = QLabel(self)
        self.indirizzo = QLabel(self)
        self.telefono = QLabel(self)
        self.completa = QLabel(self)

        self.ok = QPushButton(self)

        self.schermata()

    def schermata(self):

        global str6, str4, str3, str2, str1, str5
        if self.lingua == "Inglese":
            str1 = "Complete the following fields"
            str2 = "Surname and name"
            str3 = "Time"
            str4 = "Address"
            str5 = "Telephone"
            str6 = "Confirm"
        if self.lingua == "Italiano":
            str1 = "Completa i seguenti campi"
            str2 = "Cognome e nome"
            str3 = "Orario"
            str4 = "Indirizzo"
            str5 = "Telefono"
            str6 = "Conferma"

        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa, str1, 100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))
        self.config_label(self.cognome, str2, 170, 140, 200, 30, font)
        self.config_label(self.orario, str3, 170, 200, 200, 30, font)
        self.config_label(self.indirizzo, str4, 170, 260, 200, 30, font)
        self.config_label(self.telefono, str5, 170, 320, 200, 30, font)

        self.Config_lineEdit("Cognome", 375, 140, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.config_timeEdit("Orario", 375, 200)
        self.Config_lineEdit("Indirizzo", 375, 260, "", False, None)
        self.Config_lineEdit("Telefono", 375, 320, "", False, QRegExpValidator(QRegExp("[0-9]+")))

        self.ok.setText(str6)
        self.ok.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.ok.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.ok.move(300, 520)
        self.ok.setFixedSize(150, 30)
        self.ok.clicked.connect(self.aggiunta_delivery)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, tipo, a, b, text, flag, validatore):

        global str7
        if self.lingua == "Inglese":
            str7 = "Enter data..."
        if self.lingua == "Italiano":
            str7 = "Inserire i dati..."

        lineEdit = QLineEdit(self)
        lineEdit.setValidator(validatore)
        lineEdit.setPlaceholderText(str7)
        lineEdit.setText(text)
        lineEdit.setReadOnly(flag)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)
        self.jsonobject[tipo] = lineEdit

    def config_timeEdit(self, tipo, a, b):
        timeEdit = QTimeEdit(self)
        timeEdit.setMaximumTime(QTime(22, 00))
        timeEdit.setMinimumTime(QTime(12, 00))
        timeEdit.move(a, b)
        timeEdit.setFont(QFont("Times Roman", 15))
        timeEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        timeEdit.setFixedSize(200, 30)
        self.jsonobject[tipo] = timeEdit

    def aggiunta_delivery(self):

        global str8, str9, str10
        if self.lingua == "Inglese":
            str8 = "Fill in all fields!"
            str9 = "Impossible to book at the time entered!\nPossible times:\nlunch 12:00-14:00\ndinner 19:00-22:00"
            str10 = "Delivery order entered correctly."
        if self.lingua == "Italiano":
            str8 = "Compilare tutti i campi!"
            str9 = "Impossibile prenotare all'orario inserito!\nOrari possibili:\npranzo 12:00-14:00\ncena 19:00-22:00"
            str10 = "Ordine delivery inserito correttamente."

        cognome = self.jsonobject["Cognome"].text()
        orario = self.jsonobject["Orario"].time()
        indirizzo = self.jsonobject["Indirizzo"].text()
        telefono = self.jsonobject["Telefono"].text()
        if self.isBlank(cognome) or self.isBlank(telefono) or self.isBlank(indirizzo):
            QMessageBox.warning(None, "RGest", str8)
        elif QTime(19, 00) > orario > QTime(14, 00):
            QMessageBox.warning(None, "RGest", str9)
        else:
            ora = orario.toString(format("hh:mm"))
            self.controller.aggiungi_delivery(
                delivery_model(cognome, ora, telefono, indirizzo), orario)
            self.callback()
            self.cb_cena()
            QMessageBox.information(None, "RGest", str10)
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True
