from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QFont, QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel, QMessageBox

from Costi_covid.model.costi_covid_model import costi_covid_model
from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller


class costi_covid_view(QMainWindow):

    def __init__(self, controller):
        super(costi_covid_view, self).__init__()

        self.controller = controller
        #self.callback = callback
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

        #self.conferma = QPushButton(self)
        self.calcola = QPushButton(self)

        self.schermata()

    def schermata(self):
        validator = QRegExpValidator(QRegExp("^[0-9]+.[0-9]{1,2}"))

        self.config_label(self.completa, "Completa i seguenti campi",
                          200, 30, 750, 75, QFont("Times Roman", 20, QFont.Bold))

        self.Config_lineEdit("Scatole mascherine...", 50, 140, "", False, self.pezziMascherine, validator)
        self.Config_lineEdit("Dispenser gel...", 50, 220, "", False, self.pezziGel, validator)
        self.Config_lineEdit("Scatole guanti...", 50, 300, "", False, self.pezziGuanti, validator)
        self.Config_lineEdit("Bottiglia spray...", 50, 380, "", False, self.pezziIgienizzante, validator)
        self.Config_lineEdit("Numero disinfestazioni...", 50, 460, "", False, self.pezziDisinfestazione, validator)
        self.Config_lineEdit("Prezzo unitario...[€]", 275, 140, "", False, self.costoMascherine, validator)
        self.Config_lineEdit("Prezzo unitario...[€]", 275, 220, "", False, self.costoGel, validator)
        self.Config_lineEdit("Prezzo unitario...[€]", 275, 300, "", False, self.costoGuanti, validator)
        self.Config_lineEdit("Prezzo unitario...[€]", 275, 380, "", False, self.costoIgienizzante, validator)
        self.Config_lineEdit("Prezzo unitario...[€]", 275, 460, "", False, self.costoDisinfestazione, validator)

        self.Config_lineEdit_risultato("Mascherine", 500, 140, "")
        self.Config_lineEdit_risultato("Gel", 500, 220, "")
        self.Config_lineEdit_risultato("Guanti", 500, 300, "")
        self.Config_lineEdit_risultato("Igienizzante", 500, 380, "")
        self.Config_lineEdit_risultato("Disinfestazione", 500, 460, "")

        self.config_button("Calcola", 200, 540, self.calcola)
        self.calcola.clicked.connect(self.genera)
        #self.config_button("Conferma", 400, 440, self.conferma)
        #self.conferma.clicked.connect(self.aggiungi_ordine)

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
        lineEdit = QLineEdit(self)
        lineEdit.setPlaceholderText("Risultato...")
        lineEdit.setText(text)
        lineEdit.setReadOnly(True)
        lineEdit.move(a, b)
        lineEdit.setFont(QFont("Times Roman", 15))
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
        lineEdit.setFixedSize(200, 30)
        self.jsonobject[tipo] = lineEdit
        lineEdit.show()
        #return lineEdit

    def aggiungi_ordine(self):
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
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
        else:
            self.controller.aggiungi_covid(costi_covid_model(mascherina, gel, guanti, igienizzante, disinfestazione))
            #self.callback()
            QMessageBox.information(None, "RGest", "Ordine inserito correttamente.")
            self.controller.save_data()
            self.close()

    def genera(self):
        if self.isBlank(self.pezziMascherine.text()) or self.isBlank(self.pezziGel.text()) or self.isBlank(
            self.pezziGuanti.text()) or self.isBlank(self.pezziIgienizzante.text()) or self.isBlank(
            self.pezziDisinfestazione.text()) or self.isBlank(self.costoMascherine.text()) or self.isBlank(
            self.costoGel.text()) or self.isBlank(self.costoGuanti.text()) or self.isBlank(
            self.costoIgienizzante.text()) or self.isBlank(self.costoDisinfestazione.text()):
            QMessageBox.warning(None, "RGest", "Compilare tutti i campi!")
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
            self.config_button("Conferma", 400, 540, self.conferma)
            self.conferma.clicked.connect(self.aggiungi_ordine)
            self.conferma.show()

    def stringa(self, str1, str2):
        #if self.isBlank(str1) or self.isBlank(str2):
         #   return ""
        return str(float(str1)*float(str2))

    def isBlank(self, a):
        if a.isspace() or a == "":
            return True