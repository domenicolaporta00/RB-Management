from PyQt5.QtCore import QTime, QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox, QTimeEdit

from Prenotazioni.controller.prenotazioni_controller import prenotazioni_controller


class prenotazioni_view(QMainWindow):
    def __init__(self, prenotazione, elimina_callback):
        super(prenotazioni_view, self).__init__()
        self.pc = prenotazioni_controller(prenotazione)
        self.elimina_callback = elimina_callback

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.cognomeT = QLineEdit(self)
        self.orarioT = QTimeEdit(self)
        self.postiT = QLineEdit(self)
        self.infoT = QLineEdit(self)
        self.telefonoT = QLineEdit(self)
        self.tavoloT = QLineEdit(self)

        self.cognome = QLabel(self)
        self.posti = QLabel(self)
        self.orario = QLabel(self)
        self.info = QLabel(self)
        self.telefono = QLabel(self)
        self.tavolo = QLabel(self)
        self.completa = QLabel(self)

        self.elimina = QPushButton(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa, "Info prenotazione",
                          100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, "Cognome e nome", 180, 140, 190, 30, font)
        self.config_label(self.posti, "Posti", 180, 200, 190, 30, font)
        self.config_label(self.orario, "Orario", 180, 260, 190, 30, font)
        self.config_label(self.info, "Info extra*", 180, 320, 190, 30, font)
        self.config_label(self.telefono, "Telefono", 180, 380, 190, 30, font)
        self.config_label(self.tavolo, "Numero tavolo", 180, 440, 190, 30, font)

        self.Config_lineEdit(375, 140, self.pc.get_cognome(), False, self.cognomeT, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit(375, 200, self.pc.get_posti(), False, self.postiT, QRegExpValidator(QRegExp("[0-9]+")))
        self.config_timeEdit(375, 260, QTime.fromString(self.pc.get_orario(), format("hh:mm")), self.orarioT)
        self.Config_lineEdit(375, 320, self.pc.get_info(), False, self.infoT, None)
        self.Config_lineEdit(375, 380, self.pc.get_telefono(), False, self.telefonoT, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit(375, 440, self.pc.get_tavolo(), True, self.tavoloT, None)

        if self.pc.get_cognome()=="Tavolo vuoto!":
            self.elimina.setText("Conferma")
            self.elimina.move(300, 520)
        else:
            self.elimina.setText("Elimina")
            self.elimina.move(200, 520)
            self.conferma = QPushButton(self)
            self.conferma.setText("Conferma")
            self.conferma.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
            self.conferma.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.conferma.move(400, 520)
            self.conferma.setFixedSize(150, 30)
            self.conferma.clicked.connect(self.confirm)
        self.elimina.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.elimina.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.elimina.setFixedSize(150, 30)
        self.elimina.clicked.connect(self.reset)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, a, b, text, flag, lineEdit, validatore):
        lineEdit.setPlaceholderText("Inserire i dati...")
        lineEdit.setValidator(validatore)
        lineEdit.setText(text)
        lineEdit.setReadOnly(flag)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)

    def config_timeEdit(self, a, b, time, timeEdit):
        #timeEdit = QTimeEdit(self)
        timeEdit.setTime(time)
        timeEdit.setMaximumTime(QTime(21, 00))
        timeEdit.setMinimumTime(QTime(12, 00))
        timeEdit.move(a, b)
        timeEdit.setFont(QFont("Times Roman", 15))
        timeEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        timeEdit.setFixedSize(200, 30)

    def reset(self):
        if self.pc.get_cognome()=="Tavolo vuoto!":
            self.confirm()
        else:
            self.pc.set_cognome("Tavolo vuoto!")
            self.pc.set_posti("0")
            self.pc.set_orario("12:00")
            self.pc.set_info("")
            self.pc.set_telefono("")
            self.elimina_callback()
            QMessageBox.information(None, "RGest", "Prenotazione cancellata correttamente.")
            self.close()

    def confirm(self):
        if (self.isBlank(self.cognomeT.text()) or self.isBlank(self.postiT.text()) or self.isBlank(
                self.tavoloT.text()) or self.isBlank(self.telefonoT.text())):
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        else:
            self.pc.set_cognome(self.cognomeT.text())
            self.pc.set_posti(self.postiT.text())
            self.pc.set_orario(self.orarioT.time().toString(format("hh:mm")))
            self.pc.set_info(self.infoT.text())
            self.pc.set_telefono(self.telefonoT.text())
            self.pc.set_tavolo(self.tavoloT.text())
            self.elimina_callback()
            QMessageBox.information(None, "RGest", "Prenotazione modificata correttamente.")
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True