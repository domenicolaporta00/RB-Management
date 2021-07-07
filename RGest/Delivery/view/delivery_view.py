from PyQt5.QtCore import QTime, QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QTimeEdit, QLabel, QPushButton, QMessageBox

from Delivery.controller.delivery_controller import delivery_controller


class delivery_view(QMainWindow):
    def __init__(self, delivery, elimina_funz, elimina_callback, aggiorna, turno, lingua):
        super(delivery_view, self).__init__()

        self.lingua = lingua

        self.dc = delivery_controller(delivery)
        self.elimina_delivery = elimina_funz
        self.elimina_callback = elimina_callback
        self.aggiorna = aggiorna
        self.turno = turno

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.cognomeT = QLineEdit(self)
        self.orarioT = QTimeEdit(self)
        self.indirizzoT = QLineEdit(self)
        self.telefonoT = QLineEdit(self)

        self.cognome = QLabel(self)
        self.orario = QLabel(self)
        self.indirizzo = QLabel(self)
        self.telefono = QLabel(self)
        self.completa = QLabel(self)

        self.elimina = QPushButton(self)
        self.modifica = QPushButton(self)

        self.schermata()

    def schermata(self):

        global str6, str4, str3, str2, str1, str5, str7
        if self.lingua == "Inglese":
            str1 = "Delivery info"
            str2 = "Surname and name"
            str3 = "Time"
            str4 = "Address"
            str5 = "Telephone"
            str6 = "Delete"
            str7 = "Modification"
        if self.lingua == "Italiano":
            str1 = "Info consegna"
            str2 = "Cognome e nome"
            str3 = "Orario"
            str4 = "Indirizzo"
            str5 = "Telefono"
            str6 = "Elimina"
            str7 = "Modifica"

        font = QFont("Times Roman", 15, QFont.Bold)
        f = QFont("Times Roman", 11, QFont.Bold)

        self.config_label(self.completa, str1, 100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, str2, 170, 140, 200, 30, font)
        self.config_label(self.orario, str3, 170, 200, 190, 30, font)
        self.config_label(self.indirizzo, str4, 170, 260, 190, 30, font)
        self.config_label(self.telefono, str5, 170, 320, 190, 30, font)

        self.Config_lineEdit(375, 140, self.dc.get_cognome(), False, self.cognomeT, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.config_timeEdit(375, 200, QTime.fromString(self.dc.get_orario(), format("hh:mm")), self.orarioT)
        self.Config_lineEdit(375, 260, self.dc.get_indirizzo(), False, self.indirizzoT, None)
        self.Config_lineEdit(375, 320, self.dc.get_telefono(), False, self.telefonoT, QRegExpValidator(QRegExp("[0-9]+")))

        self.config_button(self.elimina, str6, f, 150, 30, 200, 520)
        self.config_button(self.modifica, str7, f, 150, 30, 400, 520)
        self.modifica.clicked.connect(self.confirm)
        self.elimina.clicked.connect(self.elimina_click)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, a, b, text, flag, lineEdit, validatore):

        global str8
        if self.lingua == "Inglese":
            str8 = "Enter data..."
        if self.lingua == "Italiano":
            str8 = "Inserire i dati..."

        lineEdit.setPlaceholderText(str8)
        lineEdit.setValidator(validatore)
        lineEdit.setText(text)
        lineEdit.setReadOnly(flag)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)

    def config_timeEdit(self, a, b, time, timeEdit):
        timeEdit.setTime(time)
        if self.turno == "pranzo":
            timeEdit.setMaximumTime(QTime(14, 00))
            timeEdit.setMinimumTime(QTime(12, 00))
        if self.turno == "cena":
            timeEdit.setMaximumTime(QTime(22, 00))
            timeEdit.setMinimumTime(QTime(19, 00))
        timeEdit.move(a, b)
        timeEdit.setFont(QFont("Times Roman", 15))
        timeEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        timeEdit.setFixedSize(200, 30)

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def confirm(self):

        global str11, str9, str10
        if self.lingua == "Inglese":
            str11 = "Fill in all fields!"
            str9 = "Impossible to book at the time entered!\nPossible times:\nlunch 12:00-14:00\ndinner 19:00-22:00"
            str10 = "Correctly modified delivery."
        if self.lingua == "Italiano":
            str11 = "Compilare tutti i campi!"
            str9 = "Impossibile prenotare all'orario inserito!\nOrari possibili:\npranzo 12:00-14:00\ncena 19:00-22:00"
            str10 = "Consegna modificata correttamente."

        if self.isBlank(self.cognomeT.text()) or self.isBlank(self.indirizzoT.text()) or self.isBlank(self.telefonoT.text()):
            QMessageBox.warning(None, "RGest", str11)
        elif QTime(19, 00) > self.orarioT.time() > QTime(14, 00):
            QMessageBox.warning(None, "RGest", str9)
        else:
            self.dc.set_cognome(self.cognomeT.text())
            self.dc.set_orario(self.orarioT.time().toString(format("hh:mm")))
            self.dc.set_indirizzo(self.indirizzoT.text())
            self.dc.set_telefono(self.telefonoT.text())
            self.elimina_callback()
            self.aggiorna()
            QMessageBox.information(None, "RGest", str10)
            self.close()

    def elimina_click(self):

        global str12
        if self.lingua == "Inglese":
            str12 = "Delivery deleted successfully!"
        if self.lingua == "Italiano":
            str12 = "Consegna eliminata correttamente!"

        self.elimina_delivery(self.dc.get_telefono())
        self.elimina_callback()
        self.aggiorna()
        QMessageBox.information(None, "RGest", str12)
        self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True
