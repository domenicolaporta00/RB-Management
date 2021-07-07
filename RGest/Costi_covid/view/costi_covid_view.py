from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox

from Costi_covid.model.costi_covid_model import costi_covid_model
from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller


class costi_covid_view(QMainWindow):

    def __init__(self, controller, lingua):
        super(costi_covid_view, self).__init__()

        self.lingua = lingua

        self.controller = controller
        self.jsonobject = {}

        self.lccc = lista_costi_covid_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.costoMascherine = QLineEdit(self)
        self.costoGel = QLineEdit(self)
        self.costoGuanti = QLineEdit(self)
        self.costoIgienizzante = QLineEdit(self)
        self.costoDisinfestazione = QLineEdit(self)

        self.pezziMascherine = QLineEdit(self)
        self.pezziGel = QLineEdit(self)
        self.pezziGuanti = QLineEdit(self)
        self.pezziIgienizzante = QLineEdit(self)
        self.pezziDisinfestazione = QLineEdit(self)

        self.completa = QLabel(self)

        self.calcola = QPushButton(self)

        self.schermata()

    def schermata(self):

        global str1, str2, str3, str4, str5, str6, str7, str8
        if self.lingua == "Inglese":
            str1 = "Complete the following fields"
            str2 = "Masks boxes..."
            str3 = "Gel dispenser..."
            str4 = "Glove boxes..."
            str5 = "Spray bottle..."
            str6 = "Number of disinfestations..."
            str7 = "Unit price...[€]"
            str8 = "Calculate"
        if self.lingua == "Italiano":
            str1 = "Completa i seguenti campi"
            str2 = "Scatole mascherine..."
            str3 = "Dispenser gel..."
            str4 = "Scatole guanti..."
            str5 = "Bottiglia spray..."
            str6 = "Numero di disinfestazioni..."
            str7 = "Prezzo unitario...[€]"
            str8 = "Calcola"

        validator = QRegExpValidator(QRegExp("^[0-9]+.[0-9]{1,2}"))

        self.config_label(self.completa, str1,
                          200, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.Config_lineEdit(str2, 50, 140, "", False, self.pezziMascherine, validator)
        self.Config_lineEdit(str3, 50, 220, "", False, self.pezziGel, validator)
        self.Config_lineEdit(str4, 50, 300, "", False, self.pezziGuanti, validator)
        self.Config_lineEdit(str5, 50, 380, "", False, self.pezziIgienizzante, validator)
        self.Config_lineEdit(str6, 50, 460, "", False, self.pezziDisinfestazione, validator)
        self.Config_lineEdit(str7, 275, 140, "", False, self.costoMascherine, validator)
        self.Config_lineEdit(str7, 275, 220, "", False, self.costoGel, validator)
        self.Config_lineEdit(str7, 275, 300, "", False, self.costoGuanti, validator)
        self.Config_lineEdit(str7, 275, 380, "", False, self.costoIgienizzante, validator)
        self.Config_lineEdit(str7, 275, 460, "", False, self.costoDisinfestazione, validator)

        self.Config_lineEdit_risultato("Mascherine", 500, 140, "")
        self.Config_lineEdit_risultato("Gel", 500, 220, "")
        self.Config_lineEdit_risultato("Guanti", 500, 300, "")
        self.Config_lineEdit_risultato("Igienizzante", 500, 380, "")
        self.Config_lineEdit_risultato("Disinfestazione", 500, 460, "")

        self.config_button(str8, 200, 540, self.calcola)
        self.calcola.clicked.connect(self.genera)

    def config_button(self, text, x, y, bottone):
        bottone.setText(text)
        bottone.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        bottone.setFont(QFont("Times Roman", 11, QFont.Bold))
        bottone.move(x, y)
        bottone.setFixedSize(150, 30)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def Config_lineEdit(self, pht, a, b, text, flag, lineEdit, validatore):
        lineEdit.setPlaceholderText(pht)
        lineEdit.setValidator(validatore)
        lineEdit.setText(text)
        lineEdit.setReadOnly(flag)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)

    def Config_lineEdit_risultato(self, tipo, a, b, text):

        global str1_
        if self.lingua == "Inglese":
            str1_ = "Result..."
        if self.lingua == "Italiano":
            str1_ = "Risultato..."

        lineEdit = QLineEdit(self)
        lineEdit.setPlaceholderText(str1_)
        lineEdit.setText(text)
        lineEdit.setReadOnly(True)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)
        self.jsonobject[tipo] = lineEdit
        lineEdit.show()

    def aggiungi_ordine(self):

        global _str1, _str2
        if self.lingua == "Inglese":
            _str1 = "Fill in all fields!"
            _str2 = "Order entered successfully."
        if self.lingua == "Italiano":
            _str1 = "Compilare tutti i campi!"
            _str2 = "Ordine inserito correttamente."

        mascherina = self.jsonobject["Mascherine"].text()
        gel = self.jsonobject["Gel"].text()
        guanti = self.jsonobject["Guanti"].text()
        igienizzante = self.jsonobject["Igienizzante"].text()
        disinfestazione = self.jsonobject["Disinfestazione"].text()
        if self.isBlank(self.pezziMascherine.text()) or self.isBlank(self.pezziGel.text()) or self.isBlank(
                self.pezziGuanti.text()) or self.isBlank(self.pezziIgienizzante.text()) or self.isBlank(
            self.pezziDisinfestazione.text()) or self.isBlank(self.costoMascherine.text()) or self.isBlank(
            self.costoGel.text()) or self.isBlank(self.costoGuanti.text()) or self.isBlank(
            self.costoIgienizzante.text()) or self.isBlank(self.costoDisinfestazione.text()):
            QMessageBox.warning(None, "RGest", _str1)
        else:
            self.controller.aggiungi_covid(costi_covid_model(mascherina, gel, guanti, igienizzante, disinfestazione))
            QMessageBox.information(None, "RGest", _str2)
            self.controller.save_data()
            self.close()

    def genera(self):

        global str11, str21
        if self.lingua == "Inglese":
            str11 = "Fill in all fields!"
            str21 = "Confirm"
        if self.lingua == "Italiano":
            str11 = "Compilare tutti i campi!"
            str21 = "Conferma"

        if self.isBlank(self.pezziMascherine.text()) or self.isBlank(self.pezziGel.text()) or self.isBlank(
                self.pezziGuanti.text()) or self.isBlank(self.pezziIgienizzante.text()) or self.isBlank(
            self.pezziDisinfestazione.text()) or self.isBlank(self.costoMascherine.text()) or self.isBlank(
            self.costoGel.text()) or self.isBlank(self.costoGuanti.text()) or self.isBlank(
            self.costoIgienizzante.text()) or self.isBlank(self.costoDisinfestazione.text()):
            QMessageBox.warning(None, "RGest", str11)
        else:
            mascherine = self.stringa(self.pezziMascherine.text(), self.costoMascherine.text())
            gel = self.stringa(self.pezziGel.text(), self.costoGel.text())
            guanti = self.stringa(self.pezziGuanti.text(), self.costoGuanti.text())
            igienizzante = self.stringa(self.pezziIgienizzante.text(), self.costoIgienizzante.text())
            disinfestazione = self.stringa(self.pezziDisinfestazione.text(), self.costoDisinfestazione.text())
            self.Config_lineEdit_risultato("Mascherine", 500, 140, mascherine)
            self.Config_lineEdit_risultato("Gel", 500, 220, gel)
            self.Config_lineEdit_risultato("Guanti", 500, 300, guanti)
            self.Config_lineEdit_risultato("Igienizzante", 500, 380, igienizzante)
            self.Config_lineEdit_risultato("Disinfestazione", 500, 460, disinfestazione)

            self.conferma = QPushButton(self)
            self.config_button(str21, 400, 540, self.conferma)
            self.conferma.clicked.connect(self.aggiungi_ordine)
            self.conferma.show()

    def stringa(self, str1, str2):
        return str(float(str1) * float(str2))

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True
