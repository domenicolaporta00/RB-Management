import pywhatkit
from PyQt5.QtCore import QTime
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QInputDialog, QMessageBox, QTableWidget, QTableWidgetItem

from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller


class lista_clienti_view(QMainWindow):

    def __init__(self, lingua):
        super(lista_clienti_view, self).__init__()

        self.lingua = lingua

        self.lclientic = lista_clienti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QTableWidget(self)

        self.messaggio = QPushButton(self)

        self.label = QLabel(self)

        self.schermata()

    def schermata(self):

        global str1, str2
        if self.lingua == "Inglese":
            str1 = "List of all customers"
            str2 = "Send a message"
        if self.lingua == "Italiano":
            str1 = "Elenco di tutti i clienti"
            str2 = "Invia un messaggio"

        font = QFont("Times Roman", 20, QFont.Bold)
        f = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.move(129, 100)
        self.lista.setFixedSize(492, 400)

        self.config_label(self.label, str1, 225, 40, 300, 40, font)

        self.config_button(self.messaggio, str2, f, 180, 30, 285, 550)
        self.messaggio.clicked.connect(self.invia_mex)

    def genera_lista(self):

        global str11, str21, str31
        if self.lingua == "Inglese":
            str11 = "Name"
            str21 = "Telephone"
            str31 = "First booking"
        if self.lingua == "Italiano":
            str11 = "Nome"
            str21 = "Telefono"
            str31 = "Prima prenotazione"

        self.lista.setColumnCount(3)
        self.lista.setColumnWidth(0, 150)
        self.lista.setColumnWidth(1, 150)
        self.lista.setColumnWidth(2, 150)
        self.lista.setHorizontalHeaderLabels([str11, str21, str31])
        a = 0
        for row, date in enumerate(self.lclientic.get_lista_clienti_noDoppi()):
            a += 1
            self.lista.setRowCount(a)
            item = QTableWidgetItem(date.nome)
            item2 = QTableWidgetItem(str(date.telefono))
            item3 = QTableWidgetItem(date.data)
            self.lista.setItem(row, 0, item)
            self.lista.setItem(row, 1, item2)
            self.lista.setItem(row, 2, item3)

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    '''def controllo(self, c):
        for cliente in self.clienti_noDoppi:
            if c.nome == cliente.nome and c.telefono == cliente.telefono:
                return True
        return False'''

    def invia_mex(self):

        global str52, str42, str32, str22, str12
        if self.lingua == "Inglese":
            str12 = "Empty customer list. Unable to send messages."
            str22 = "Write your message. (Warning! The procedure can take\na long time and cannot be done" \
                    "in the background.\nIt is recommended to run outside business hours!\nPress ok to" \
                    "to continue!) "
            str32 = "Type something!"
            str42 = "The system will open whatsapp web for each custom stored and there will be twenty seconds to" \
                    "provision to frame the QR code; at the end of twenty seconds the message will be sent" \
                    "correctly and you will go to the next one. Do not interact with the application while sending the" \
                    "messages! "
            str52 = "Sending messages finished."
        if self.lingua == "Italiano":
            str12 = "Lista clienti vuota. Impossibile inviare messaggi."
            str22 = "Scrivi il messaggio. (Attenzione! La procedura può impiegare\ntanto tempo e non può essere fatta " \
                    "in background.\nSi consiglia di eseguire fuori dall'orario lavorativo!\nPremere ok per " \
                    "continuare!) "
            str32 = "Digitare qualcosa!"
            str42 = "Il sistema aprirà whatsapp web per ogni cliente memorizzato e ci saranno venti secondi a " \
                    "disposizione per inquadrare il QR code; al termine dei venti secondi il messaggio verrà inviato " \
                    "correttamente e si passerà al successivo. Non interagire con l'applicazione durante l'invio dei " \
                    "messaggi! "
            str52 = "Invio messaggi terminato."

        if not self.lclientic.get_lista_clienti():
            QMessageBox.warning(None, "RGest", str12)
        else:
            text, select = QInputDialog.getText(None, "RGest", str22)
            if not select:
                pass
            else:
                if not text:
                    QMessageBox.warning(None, "RGest", str32)
                else:
                    QMessageBox.warning(None, "RGest", str42)
                    self.close()
                    for cliente in self.lclientic.get_lista_clienti():
                        ora = QTime.currentTime().hour()
                        minuto = QTime.currentTime().minute() + 1
                        if minuto == 60:
                            minuto = 0
                            ora += 1
                        else:
                            mex = "Car* " + cliente.nome + ", " + text
                            pywhatkit.sendwhatmsg("+39" + cliente.telefono, mex, ora, minuto)
                    QMessageBox.information(None, "RGest", str52)
