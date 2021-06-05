from PyQt5.QtGui import QIcon, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QListView, QMessageBox

from Cliente.model.cliente_model import cliente_model
from Coperti.model.coperti_model import coperti_model
from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller
from Lista_coperti.controller.lista_coperti_controller import lista_coperti_controller
from Lista_prenotazioni.controller.lista_prenotazioni_controller import lista_prenotazioni_controller
from Lista_prenotazioni.view.inserisci_prenotazione_view import inserisci_prenotazione_view
from Prenotazioni.view.prenotazioni_view import prenotazioni_view


class lista_prenotazioni_view(QMainWindow):

    def __init__(self):
        super(lista_prenotazioni_view, self).__init__()

        self.lpc = lista_prenotazioni_controller()
        self.lcc = lista_coperti_controller()
        self.lclientic = lista_clienti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

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

        self.config_button(self.aggiungi, "Aggiungi", font, 150, 30, 45, 550)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.visualizza, "Modifica", font, 150, 30, 555, 550)
        self.visualizza.clicked.connect(self.mostra_prenotazione)
        self.config_button(self.elimina, "Elimina tutto", font, 150, 30, 215, 550)
        self.elimina.clicked.connect(self.cancel)
        self.config_button(self.salva, "Termina giornata", font, 150, 30, 385, 550)
        self.salva.clicked.connect(self.termina)

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

    def termina(self):
        n = 0
        for prenotazioni in self.lpc.get_lista_prenotazioni():
            n += int(prenotazioni.posti)
        self.lcc.aggiungi_coperto(coperti_model(n))
        for prenotazioni in self.lpc.get_lista_prenotazioni():
            if prenotazioni.cognome == "Tavolo vuoto!":
                print("vuoto")
            else:
                if self.controllo(cliente_model(prenotazioni.cognome, prenotazioni.telefono)):
                    print("c'è già")
                else:
                    self.lclientic.aggiungi_cliente(cliente_model(prenotazioni.cognome, prenotazioni.telefono))
        self.lpc.cancel()
        self.genera_lista()
        QMessageBox.information(None, "RGest", "Giornata terminata! Il numero dei coperti e i contatti dei clienti "
                                               "sono stati salvati correttamente!")
        self.close()

    def controllo(self, c):
        for cliente in self.lclientic.get_lista_clienti():
            if c.nome == cliente.nome and c.telefono == cliente.telefono:
                return True
        return False

    def closeEvent(self, event):
        self.lpc.save_data()
        self.lcc.save_data()
        self.lclientic.save_data()



