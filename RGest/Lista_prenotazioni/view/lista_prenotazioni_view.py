from PyQt5.QtGui import QIcon, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QListWidget, QPushButton, QLabel, QListView, QMessageBox

from Lista_prenotazioni.controller.lista_prenotazioni_controller import lista_prenotazioni_controller
from Lista_prenotazioni.view.inserisci_prenotazione_view import inserisci_prenotazione_view
from Prenotazioni.view.prenotazioni_view import prenotazioni_view


class lista_prenotazioni_view(QMainWindow):

    def __init__(self):
        super(lista_prenotazioni_view, self).__init__()

        self.lpc = lista_prenotazioni_controller()

        #self.ipv = inserisci_prenotazione_view(self.lpc, self.genera_lista)

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.numero_posti = 0

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QListView(self)

        self.aggiungi = QPushButton(self)
        self.visualizza = QPushButton(self)
        self.elimina = QPushButton(self)
        self.salva = QPushButton(self)

        self.lista_label = QLabel(self)
        self.posti_prenotati = QLabel(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lista.move(125, 100)
        self.lista.setFixedSize(500, 400)

        self.lista_label.setText("Elenco delle prenotazioni")
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(200, 40)
        self.lista_label.setFixedSize(350, 40)

        self.config_button(self.aggiungi, "Aggiungi", font, 150, 30, 100, 550)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.visualizza, "Modifica", font, 150, 30, 500, 550)
        self.visualizza.clicked.connect(self.mostra_prenotazione)
        self.config_button(self.elimina, "Elimina tutto", font, 150, 30, 300, 550)
        self.elimina.clicked.connect(self.cancel)

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def apri_inserimento(self):
        self.newelement()

    def genera_lista(self):
        self.list_view_model = QStandardItemModel(self.lista)
        for prenotazione in self.lpc.get_lista_prenotazioni():
            item = QStandardItem()
            item.setText(prenotazione.cognome + " Tavolo: " + prenotazione.tavolo)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
        self.lista.setModel(self.list_view_model)

    def mostra_prenotazione(self):
        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare una prenotazione!")
        else:
            selected = self.lista.selectedIndexes()[0].row()
            prenotazione_selezionata = self.lpc.get_prenotazione(selected)
            #print(prenotazione_selezionata.tavolo)
            self.pv = prenotazioni_view(prenotazione_selezionata, self.genera_lista)
            self.pv.show()

    def cancel(self):
        self.lpc.cancel()
        self.lpc.save_data()
        self.genera_lista()
        QMessageBox.information(None, "RGest", "Tutte le prenotazioni sono state cancellate!")

    def newelement(self):
        self.closeEvent(self.lpc.save_data())
        self.ipv = inserisci_prenotazione_view(self.lpc, self.genera_lista)
        self.ipv.show()

    def closeEvent(self, event):
        self.lpc.save_data()



