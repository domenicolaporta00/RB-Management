from PyQt5.QtGui import QIcon, QFont, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QListView, QMessageBox, QTabWidget, QWidget, QVBoxLayout, \
    QHBoxLayout

from Cliente.model.cliente_model import cliente_model
from Coperti.model.coperti_model import coperti_model
from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller
from Lista_comande.controller.lista_comande_controller import lista_comande_controller
from Lista_coperti.controller.lista_coperti_controller import lista_coperti_controller
from Lista_prenotazioni.controller.lista_prenotazioni_controller import lista_prenotazioni_controller
from Lista_prenotazioni.view.inserisci_prenotazione_view import inserisci_prenotazione_view
from Prenotazioni.view.prenotazioni_view import prenotazioni_view


class lista_prenotazioni_view(QMainWindow):

    def __init__(self):
        super(lista_prenotazioni_view, self).__init__()

        # self.lcomandec = lista_comande_controller()
        self.lpc = lista_prenotazioni_controller()
        self.lcc = lista_coperti_controller()
        self.lclientic = lista_clienti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.tab_widget = QTabWidget(self)
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)

        self.lista = QListView(self)
        self.lista_cena = QListView(self)

        self.aggiungi = QPushButton(self)
        self.visualizza = QPushButton(self)
        self.visualizza_cena = QPushButton(self)
        self.elimina = QPushButton(self)
        self.salva = QPushButton(self)

        self.lista_label = QLabel(self)
        self.posti_prenotati = QLabel(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11, QFont.Bold)

        self.tab_widget.setFixedSize(700, 450)
        self.tab_widget.move(25, 75)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, "Pranzo")
        self.tab_widget.addTab(self.tab2, "Cena")

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.genera_lista_cena()
        self.lista_cena.setModel(self.list_view_model_cena)
        self.lista_cena.setStyleSheet("background-color: rgb(255, 255, 255)")
        # self.lista.move(125, 100)
        # self.lista.setFixedSize(500, 400)

        layout1 = QVBoxLayout(self)
        layout1.addWidget(self.lista)
        layout1.addWidget(self.visualizza)
        self.tab1.setLayout(layout1)

        layout2 = QVBoxLayout(self)
        layout2.addWidget(self.lista_cena)
        layout2.addWidget(self.visualizza_cena)
        self.tab2.setLayout(layout2)

        self.lista_label.setText("Elenco delle prenotazioni")
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(200, 40)
        self.lista_label.setFixedSize(350, 40)

        self.config_button(self.visualizza, "Modifica", font, 150, 30, 36, 550)
        self.visualizza.clicked.connect(self.mostra_prenotazione)
        self.config_button(self.visualizza_cena, "Modifica", font, 150, 30, 36, 550)
        self.visualizza_cena.clicked.connect(self.mostra_prenotazione_cena)
        self.config_button(self.aggiungi, "Aggiungi", font, 150, 30, 211, 482)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.elimina, "Elimina tutto", font, 150, 30, 387, 482)
        self.elimina.clicked.connect(self.cancel)
        self.config_button(self.salva, "Termina giornata", font, 150, 30, 562, 482)
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
            item.setText(prenotazione.cognome + " Tavolo: " + str(prenotazione.tavolo))
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
        self.lista.setModel(self.list_view_model)

    def genera_lista_cena(self):
        self.list_view_model_cena = QStandardItemModel(self.lista_cena)
        for prenotazione in self.lpc.get_lista_prenotazioni_cena():
            item = QStandardItem()
            item.setText(prenotazione.cognome + " Tavolo: " + str(prenotazione.tavolo))
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model_cena.appendRow(item)
        self.lista_cena.setModel(self.list_view_model_cena)

    def mostra_prenotazione(self):
        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare una prenotazione!")
        else:
            selected = self.lista.selectedIndexes()[0].row()
            prenotazione_selezionata = self.lpc.get_prenotazione(selected)
            self.pv = prenotazioni_view(prenotazione_selezionata, self.genera_lista, self.genera_lista_cena, "pranzo")
            self.pv.show()

    def mostra_prenotazione_cena(self):
        if not self.lista_cena.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare una prenotazione!")
        else:
            selected_ = self.lista_cena.selectedIndexes()[0].row()
            prenotazione_selezionata_ = self.lpc.get_prenotazione_cena(selected_)
            self.pv = prenotazioni_view(prenotazione_selezionata_, self.genera_lista, self.genera_lista_cena, "cena")
            self.pv.show()

    def cancel(self):
        self.lpc.cancel()
        self.lpc.cancel_cena()
        self.lpc.save_data()
        self.genera_lista()
        self.genera_lista_cena()
        QMessageBox.information(None, "RGest", "Tutte le prenotazioni sono state cancellate!")

    def newelement(self):
        self.closeEvent(self.lpc.save_data())
        self.ipv = inserisci_prenotazione_view(self.lpc, self.genera_lista, self.genera_lista_cena)
        self.ipv.show()

    def termina(self):
        n = 0
        for prenotazioni in self.lpc.get_lista_prenotazioni():
            n += int(prenotazioni.posti)
        #self.lcc.aggiungi_coperto(coperti_model(n))
        for prenotazioni in self.lpc.get_lista_prenotazioni():
            if prenotazioni.cognome == "Tavolo vuoto!":
                pass
            else:
                if self.controllo(cliente_model(prenotazioni.cognome, prenotazioni.telefono)):
                    pass
                else:
                    self.lclientic.aggiungi_cliente(cliente_model(prenotazioni.cognome, prenotazioni.telefono))
        for prenotazioni in self.lpc.get_lista_prenotazioni_cena():
            n += int(prenotazioni.posti)
        self.lcc.aggiungi_coperto(coperti_model(n))
        for prenotazioni in self.lpc.get_lista_prenotazioni_cena():
            if prenotazioni.cognome == "Tavolo vuoto!":
                pass
            else:
                if self.controllo(cliente_model(prenotazioni.cognome, prenotazioni.telefono)):
                    pass
                else:
                    self.lclientic.aggiungi_cliente(cliente_model(prenotazioni.cognome, prenotazioni.telefono))
        self.lpc.cancel()
        self.lpc.cancel_cena()
        self.genera_lista()
        self.genera_lista_cena()
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
