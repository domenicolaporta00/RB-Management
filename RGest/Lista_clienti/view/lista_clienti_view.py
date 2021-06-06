import time

from PyQt5.QtCore import QTime, Qt
from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtWidgets import QMainWindow, QListView, QPushButton, QLabel, QInputDialog, QMessageBox, QSplashScreen, \
    QProgressBar

from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller

import pywhatkit

from Lista_prenotazioni.view.lista_prenotazioni_view import lista_prenotazioni_view
from Tasse.view.tasse_view import tasse_view


class lista_clienti_view(QMainWindow):

    def __init__(self):
        super(lista_clienti_view, self).__init__()

        self.lclientic = lista_clienti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QListView(self)

        self.messaggio = QPushButton(self)

        self.label = QLabel(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 20, QFont.Bold)
        f = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0)")
        self.lista.move(75, 100)
        self.lista.setFixedSize(600, 400)

        self.config_label(self.label, "Elenco di tutti i clienti", 225, 40, 300, 40, font)

        self.config_button(self.messaggio, "Invia un messaggio", f, 180, 30, 285, 550)
        self.messaggio.clicked.connect(self.invia_mex)

    def genera_lista(self):
        #self.lclientic.cancel()
        #self.lclientic.save_data()
        self.list_view_model = QStandardItemModel(self.lista)
        for cliente in self.lclientic.get_lista_clienti():
            item = QStandardItem()
            item.setText(cliente.nome + " " + cliente.telefono + " prima prenotazione " + cliente.data)
            item.setEditable(False)
            item.setEnabled(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
        self.lista.setModel(self.list_view_model)

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

    def invia_mex(self):
        if not self.lclientic.get_lista_clienti():
            QMessageBox.warning(None, "RGest", "Lista clienti vuota. Impossibile inviare messaggi.")
        else:
            text, select = QInputDialog.getText(None, "RGest",
                                                "Scrivi il messaggio. (Attenzione! La procedura può impiegare\ntanto "
                                                "tempo "
                                                "e non può essere fatta "
                                                "in background.\nSi consiglia di eseguire fuori dall'orario "
                                                "lavorativo!\n"
                                                "Premere ok per continuare!)")
            if not select:
                pass
            else:
                if not text:
                    QMessageBox.warning(None, "RGest", "Digitare qualcosa!")
                else:
                    QMessageBox.warning(None, "RGest",
                                        "Il sistema aprirà whatsapp web per ogni cliente memorizzato e ci "
                                        "saranno venti secondi a disposizione per inquadrare il QR code; "
                                        "al termine dei venti secondi il messaggio verrà inviato "
                                        "correttamente e si passerà al successivo. Non interagire con "
                                        "l'applicazione durante l'invio dei messaggi!")
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
                    QMessageBox.information(None, "RGest", "Invio messaggi terminato.")


