from PyQt5.QtCore import QTime, QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QTimeEdit

from Lista_prenotazioni.controller.lista_prenotazioni_controller import lista_prenotazioni_controller
from Prenotazioni.model.prenotazioni_model import prenotazioni_model


class inserisci_prenotazione_view(QMainWindow):

    def __init__(self, controller, callback, cb_cena):
        super(inserisci_prenotazione_view, self).__init__()

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
        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa,
                          "            Completa i seguenti campi \n(contrassegnato con * non obbligatorio)",
                          100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, "Cognome e nome", 180, 140, 200, 30, font)
        self.config_label(self.posti, "Posti", 180, 200, 200, 30, font)
        self.config_label(self.orario, "Orario", 180, 260, 200, 30, font)
        self.config_label(self.info, "Info extra*", 180, 320, 200, 30, font)
        self.config_label(self.telefono, "Telefono", 180, 380, 200, 30, font)
        self.config_label(self.tavolo, "Numero tavolo", 180, 440, 200, 30, font)

        self.Config_lineEdit("Cognome", 375, 140, "", False, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit("Posti", 375, 200, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.config_timeEdit("Orario", 375, 260)
        self.Config_lineEdit("Info extra", 375, 320, "", False, None)
        self.Config_lineEdit("Telefono", 375, 380, "", False, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit("Numero tavolo", 375, 440, "", True, None)
        # str(len(self.lpc.get_lista_prenotazioni()) + 1)
        self.ok.setText("Conferma")
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
        cognome = self.jsonobject["Cognome"].text()
        posti = self.jsonobject["Posti"].text()
        orario = self.jsonobject["Orario"].time()
        info = self.jsonobject["Info extra"].text()
        telefono = self.jsonobject["Telefono"].text()
        #num_tavoli = self.jsonobject["Numero tavolo"].text()
        if self.isBlank(cognome) or self.isBlank(posti) or self.isBlank(telefono):
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        elif QTime(19, 00) > orario > QTime(14, 00):
            QMessageBox.warning(None, "RGest", "Impossibile prenotare all'orario inserito!\nOrari "
                                               "possibili:\npranzo 12:00-14:00\ncena 19:00-22:00")
        else:
            ora = orario.toString(format("hh:mm"))
            num_tavoli = 0
            if QTime(14, 00) >= orario >= QTime(12, 00):
                num_tavoli = len(self.lpc.get_lista_prenotazioni()) + 1
            if QTime(22, 00) >= orario >= QTime(19, 00):
                num_tavoli = len(self.lpc.get_lista_prenotazioni_cena()) + 1
            self.controller.aggiungi_prenotazione(
                prenotazioni_model(cognome, posti, ora, info, telefono, num_tavoli), orario)
            self.callback()
            self.cb_cena()
            QMessageBox.information(None, "RGest", "Prenotazione inserita correttamente.")
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True
