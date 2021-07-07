from PyQt5.QtCore import QTime, QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QTimeEdit

from Lista_prenotazioni.controller.lista_prenotazioni_controller import lista_prenotazioni_controller
from Prenotazioni.model.prenotazioni_model import prenotazioni_model


class inserisci_prenotazione_view(QMainWindow):

    def __init__(self, controller, callback, cb_cena, lingua):
        super(inserisci_prenotazione_view, self).__init__()

        self.lingua = lingua

        self.controller = controller
        self.callback = callback
        self.cb_cena = cb_cena
        self.jsonobject = {}

        self.lpc = lista_prenotazioni_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.cognome = QLabel(self)
        self.posti = QLabel(self)
        self.orario = QLabel(self)
        self.info = QLabel(self)
        self.telefono = QLabel(self)
        self.tavolo = QLabel(self)
        self.completa = QLabel(self)

        self.ok = QPushButton(self)

        self.schermata()

    def schermata(self):

        global str6, str4, str3, str2, str1, str5, str7
        if self.lingua == "Inglese":
            str1 = "Complete the following fields\n(marked with * not required)"
            str2 = "Surname and name"
            str3 = "Time"
            str4 = "Seats"
            str5 = "Telephone"
            str6 = "Confirm"
            str7 = "Table number"
        if self.lingua == "Italiano":
            str1 = "Completa i seguenti campi \n(contrassegnato con * non obbligatorio)"
            str2 = "Cognome e nome"
            str3 = "Orario"
            str4 = "Posti"
            str5 = "Telefono"
            str6 = "Conferma"
            str7 = "Numero tavolo"

        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa, str1, 100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, str2, 170, 140, 200, 30, font)
        self.config_label(self.posti, str4, 170, 200, 200, 30, font)
        self.config_label(self.orario, str3, 170, 260, 200, 30, font)
        self.config_label(self.info, "Info extra*", 170, 320, 200, 30, font)
        self.config_label(self.telefono, str5, 170, 380, 200, 30, font)
        self.config_label(self.tavolo, str7, 170, 440, 200, 30, font)

        self.Config_lineEdit("Cognome", 375, 140, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit("Posti", 375, 200, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.config_timeEdit("Orario", 375, 260)
        self.Config_lineEdit("Info extra", 375, 320, "", False, None)
        self.Config_lineEdit("Telefono", 375, 380, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit("Numero tavolo", 375, 440, "", True, None)

        self.ok.setText(str6)
        self.ok.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.ok.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.ok.move(300, 520)
        self.ok.setFixedSize(150, 30)
        self.ok.clicked.connect(self.aggiunta_prenotazione)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, tipo, a, b, text, flag, validatore):

        global str8
        if self.lingua == "Inglese":
            str8 = "Enter data..."
        if self.lingua == "Italiano":
            str8 = "Inserire i dati..."

        lineEdit = QLineEdit(self)
        lineEdit.setValidator(validatore)
        lineEdit.setPlaceholderText(str8)
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

    def aggiunta_prenotazione(self):

        global str11, str9, str10
        if self.lingua == "Inglese":
            str11 = "Fill in all fields!"
            str9 = "Impossible to book at the time entered!\nPossible times:\nlunch 12:00-14:00\ndinner 19:00-22:00"
            str10 = "Booking entered correctly."
        if self.lingua == "Italiano":
            str11 = "Compilare tutti i campi!"
            str9 = "Impossibile prenotare all'orario inserito!\nOrari possibili:\npranzo 12:00-14:00\ncena 19:00-22:00"
            str10 = "Prenotazione inserita correttamente."

        cognome = self.jsonobject["Cognome"].text()
        posti = self.jsonobject["Posti"].text()
        orario = self.jsonobject["Orario"].time()
        info = self.jsonobject["Info extra"].text()
        telefono = self.jsonobject["Telefono"].text()
        if self.isBlank(cognome) or self.isBlank(posti) or self.isBlank(telefono):
            QMessageBox.warning(None, "RGest", str11)
        elif QTime(19, 00) > orario > QTime(14, 00):
            QMessageBox.warning(None, "RGest", str9)
        else:
            ora = orario.toString(format("hh:mm"))
            num_tavoli = 0
            if QTime(14, 00) >= orario >= QTime(12, 00):
                num_tavoli = len(self.lpc.get_lista_prenotazioni()) + 1
            if QTime(22, 00) >= orario >= QTime(19, 00):
                num_tavoli = len(self.lpc.get_lista_prenotazioni_cena()) + 1
            self.controller.aggiungi_prenotazione(
                prenotazioni_model(cognome, posti, ora, info, telefono, num_tavoli), orario)
            # self.lcomandec.save_data()
            self.callback()
            self.cb_cena()
            QMessageBox.information(None, "RGest", str10)
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True