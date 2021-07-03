from PyQt5.QtCore import QTime, QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox, QTimeEdit

from Prenotazioni.controller.prenotazioni_controller import prenotazioni_controller


class prenotazioni_view(QMainWindow):
    def __init__(self, prenotazione, elimina_callback, aggiorna, turno, lingua):
        super(prenotazioni_view, self).__init__()

        self.lingua = lingua

        self.pc = prenotazioni_controller(prenotazione)
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

        global str6, str4, str3, str2, str1, str5, str7, str8, str9
        if self.lingua == "Inglese":
            str1 = "Booking info"
            str2 = "Surname and name"
            str3 = "Time"
            str4 = "Seats"
            str5 = "Telephone"
            str6 = "Delete"
            str7 = "Confirm"
            str8 = "Table number"
            str9 = "Empty table!"
        if self.lingua == "Italiano":
            str1 = "Info prenotazione"
            str2 = "Cognome e nome"
            str3 = "Orario"
            str4 = "Posti"
            str5 = "Telefono"
            str6 = "Elimina"
            str7 = "Conferma"
            str8 = "Numero tavolo"
            str9 = "Tavolo vuoto!"

        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.completa, str1,
                          100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, str2, 170, 140, 190, 30, font)
        self.config_label(self.posti, str4, 170, 200, 190, 30, font)
        self.config_label(self.orario, str3, 170, 260, 190, 30, font)
        self.config_label(self.info, "Info extra*", 170, 320, 190, 30, font)
        self.config_label(self.telefono, str5, 170, 380, 190, 30, font)
        self.config_label(self.tavolo, str8, 170, 440, 190, 30, font)

        self.Config_lineEdit(375, 140, self.pc.get_cognome(), False, self.cognomeT,
                             QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit(375, 200, self.pc.get_posti(), False, self.postiT, QRegExpValidator(QRegExp("[0-9]+")))
        self.config_timeEdit(375, 260, QTime.fromString(self.pc.get_orario(), format("hh:mm")), self.orarioT)
        self.Config_lineEdit(375, 320, self.pc.get_info(), False, self.infoT, None)
        self.Config_lineEdit(375, 380, self.pc.get_telefono(), False, self.telefonoT,
                             QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit(375, 440, str(self.pc.get_tavolo()), True, self.tavoloT, None)

        if self.pc.get_cognome() == str9:
            self.elimina.setText(str7)
            self.elimina.move(300, 520)
        else:
            self.elimina.setText(str6)
            self.elimina.move(200, 520)
            self.conferma = QPushButton(self)
            self.conferma.setText(str7)
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

        global str10
        if self.lingua == "Inglese":
            str10 = "Enter data..."
        if self.lingua == "Italiano":
            str10 = "Inserire i dati..."

        lineEdit.setPlaceholderText(str10)
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

    def reset(self):

        global str11, str12
        if self.lingua == "Inglese":
            str11 = "Empty table!"
            str12 = "Booking canceled successfully."
        if self.lingua == "Italiano":
            str11 = "Tavolo vuoto!"
            str12 = "Prenotazione cancellata correttamente."

        if self.pc.get_cognome() == "Tavolo vuoto!":
            self.confirm()
        else:
            self.pc.set_cognome(str11)
            self.pc.set_posti("0")
            self.pc.set_orario("12:00")
            self.pc.set_info("")
            self.pc.set_telefono("")
            self.elimina_callback()
            self.aggiorna()
            QMessageBox.information(None, "RGest", str12)
            self.close()

    def confirm(self):

        global str13, str14, str15
        if self.lingua == "Inglese":
            str13 = "Fill in all fields!"
            str14 = "Impossible to book at the time entered!\nPossible times:\nlunch 12:00-14:00\ndinner 19:00-22:00"
            str15 = "Correctly modified booking."
        if self.lingua == "Italiano":
            str13 = "Compilare tutti i campi!"
            str14 = "Impossibile prenotare all'orario inserito!\nOrari possibili:\npranzo 12:00-14:00\ncena 19:00-22:00"
            str15 = "Prenotazione modificata correttamente."

        if (self.isBlank(self.cognomeT.text()) or self.isBlank(self.postiT.text()) or self.isBlank(
                self.tavoloT.text()) or self.isBlank(self.telefonoT.text())):
            QMessageBox.warning(None, "RGest", str13)
        elif QTime(19, 00) > self.orarioT.time() > QTime(14, 00):
            QMessageBox.warning(None, "RGest", str14)
        else:
            self.pc.set_cognome(self.cognomeT.text())
            self.pc.set_posti(self.postiT.text())
            self.pc.set_orario(self.orarioT.time().toString(format("hh:mm")))
            self.pc.set_info(self.infoT.text())
            self.pc.set_telefono(self.telefonoT.text())
            self.pc.set_tavolo(self.tavoloT.text())
            self.elimina_callback()
            self.aggiorna()
            QMessageBox.information(None, "RGest", str15)
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True
