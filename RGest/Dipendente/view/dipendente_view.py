from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QMessageBox

from Dipendente.controller.dipendente_controller import dipendente_controller
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller


class dipendente_view(QMainWindow):
    def __init__(self, dipendente, elimina, elimina_callback, lingua):
        super(dipendente_view, self).__init__()

        self.lingua = lingua

        self.dc = dipendente_controller(dipendente)
        self.elimina_callback = elimina_callback
        self.elimina_dipendente = elimina
        #self.ldc = lista_dipendenti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.cognomeT = QLineEdit(self)
        self.nomeT = QLineEdit(self)
        self.etaT = QLineEdit(self)
        self.ruoloT = QLineEdit(self)
        self.postazioneT = QLineEdit(self)
        self.stipendioT = QLineEdit(self)
        self.telefonoT = QLineEdit(self)
        self.idT = QLineEdit(self)

        self.cognome = QLabel(self)
        self.nome = QLabel(self)
        self.eta = QLabel(self)
        self.ruolo = QLabel(self)
        self.postazione = QLabel(self)
        self.stipendio = QLabel(self)
        self.telefono = QLabel(self)
        self.id = QLabel(self)
        self.informazione = QLabel(self)

        self.elimina = QPushButton(self)
        self.modifica = QPushButton(self)

        self.schermata()

    def schermata(self):

        global str1, str8, str7, str6, str5, str4, str3, str2, str9, str11, str12, str13, str14, str15, str16, str10
        if self.lingua == "Inglese":
            str1 = "Employee info"
            str2 = "Surname"
            str3 = "Name"
            str4 = "Age"
            str5 = "Station"
            str6 = "Role"
            str7 = "Telephone"
            str8 = "Salary[€]"
            str9 = "Delete"
            str10 = "Modification"
        if self.lingua == "Italiano":
            str1 = "Info dipendente"
            str2 = "Cognome"
            str3 = "Nome"
            str4 = "Età"
            str5 = "Postazione"
            str6 = "Ruolo"
            str7 = "Telefono"
            str8 = "Stipendio[€]"
            str9 = "Elimina"
            str10 = "Modifica"

        font = QFont("Times Roman", 15, QFont.Bold)

        self.config_label(self.informazione, str1, 100, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.config_label(self.cognome, str2, 180, 140, 190, 30, font)
        self.config_label(self.nome, str3, 180, 190, 190, 30, font)
        self.config_label(self.eta, str4, 180, 240, 190, 30, font)
        self.config_label(self.ruolo, str6, 180, 290, 190, 30, font)
        self.config_label(self.postazione, str5, 180, 340, 190, 30, font)
        self.config_label(self.stipendio, str8, 180, 390, 190, 30, font)
        self.config_label(self.telefono, str7, 180, 440, 190, 30, font)
        self.config_label(self.id, "Id", 180, 490, 190, 30, font)

        self.Config_lineEdit(375, 140, self.dc.get_cognome(), False, self.cognomeT, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit(375, 190, self.dc.get_nome(), False, self.nomeT, QRegExpValidator(QRegExp("[a-z-A-Z- ]+")))
        self.Config_lineEdit(375, 240, self.dc.get_eta(), False, self.etaT, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit(375, 290, self.dc.get_ruolo(), True, self.ruoloT, None)
        self.Config_lineEdit(375, 340, self.dc.get_postazione(), True, self.postazioneT, None)
        self.Config_lineEdit(375, 390, self.dc.get_stipendio(), False, self.stipendioT, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit(375, 440, self.dc.get_telefono(), False, self.telefonoT, QRegExpValidator(QRegExp("[0-9]+")))
        self.Config_lineEdit(375, 490, self.dc.get_id(), True, self.idT, None)

        self.elimina.setText(str9)
        self.elimina.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.elimina.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.elimina.move(200, 560)
        self.elimina.setFixedSize(150, 30)
        self.elimina.clicked.connect(self.elimina_click)
        self.modifica.setText(str10)
        self.modifica.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.modifica.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.modifica.move(400, 560)
        self.modifica.setFixedSize(150, 30)
        self.modifica.clicked.connect(self.modifica_click)

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

    def elimina_click(self):

        global str11
        if self.lingua == "Inglese":
            str11 = "Employee successfully deleted!"
        if self.lingua == "Italiano":
            str11 = "Dipendente eliminato correttamente!"

        self.elimina_dipendente(self.dc.get_id())
        self.elimina_callback()
        QMessageBox.information(None, "RGest", str11)
        self.close()

    def modifica_click(self):

        global str18, str20, str21, str22
        if self.lingua == "Inglese":
            str18 = "Fill in all fields!"
            str20 = "Child labor not allowed!"
            str21 = "The new employee should already be retired! Impossible to add a person with this age!"
            str22 = "Employee entered correctly."
        if self.lingua == "Italiano":
            str18 = "Compilare tutti i campi!"
            str20 = "Lavoro minorile non ammesso!"
            str21 = "Il nuovo dipendente dovrebbe già essere in pensione! Impossibile aggiungere una persona con " \
                    "questa età! "
            str22 = "Dipendente inserito correttamente."

        if self.isBlank(self.cognomeT.text()) or self.isBlank(self.nomeT.text()) or self.isBlank(self.etaT.text()) or self.isBlank(self.stipendioT.text()) or self.isBlank(self.telefonoT.text()):
            QMessageBox.warning(None, "RGest", str18)
        elif int(self.etaT.text()) < 14:
            QMessageBox.critical(None, "RGest", str20)
        elif int(self.etaT.text()) > 67:
            QMessageBox.critical(None, "RGest", str21)
        else:
            self.dc.set_cognome(self.cognomeT.text())
            self.dc.set_nome(self.nomeT.text())
            self.dc.set_eta(self.etaT.text())
            self.dc.set_stipendio(self.stipendioT.text())
            self.dc.set_telefono(self.telefonoT.text())
            self.dc.set_id(self.cognomeT.text()[:1]+""+self.nomeT.text()[:1]+self.telefonoT.text())
            self.elimina_callback()
            QMessageBox.information(None, "RGest", str22)
            self.close()

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True


