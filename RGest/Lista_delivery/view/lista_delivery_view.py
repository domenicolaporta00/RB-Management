from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QListView, QPushButton, QLabel, QVBoxLayout, QMessageBox

from Cliente.model.cliente_model import cliente_model
from Consegna_delivery.model.consegna_delivery_model import consegna_delivery_model
from Delivery.view.delivery_view import delivery_view
from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller
from Lista_coperti.controller.lista_coperti_controller import lista_coperti_controller
from Lista_delivery.controller.lista_delivery_controller import lista_delivery_controller
from Lista_delivery.view.inserisci_delivery_view import inserisci_delivery_view


class lista_delivery_view(QMainWindow):

    def __init__(self, lingua):
        super(lista_delivery_view, self).__init__()

        self.lingua = lingua

        self.ldc = lista_delivery_controller()
        self.lcopertic = lista_coperti_controller()
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

        layout1 = QVBoxLayout(self)
        layout1.addWidget(self.lista)
        layout1.addWidget(self.visualizza)
        self.tab1.setLayout(layout1)

        layout2 = QVBoxLayout(self)
        layout2.addWidget(self.lista_cena)
        layout2.addWidget(self.visualizza_cena)
        self.tab2.setLayout(layout2)

        self.lista_label.setText("Elenco delivery")
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(250, 40)
        self.lista_label.setFixedSize(250, 40)

        self.config_button(self.visualizza, "Modifica", font, 150, 30, 36, 550)
        self.visualizza.clicked.connect(self.mostra_delivery)
        self.config_button(self.visualizza_cena, "Modifica", font, 150, 30, 36, 550)
        self.visualizza_cena.clicked.connect(self.mostra_delivery_cena)
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
        for delivery in self.ldc.get_lista_delivery():
            item = QStandardItem()
            item.setText(delivery.cognome + ", " + delivery.indirizzo + ", ore " + delivery.orario)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
        self.lista.setModel(self.list_view_model)

    def genera_lista_cena(self):
        self.list_view_model_cena = QStandardItemModel(self.lista_cena)
        for delivery in self.ldc.get_lista_delivery_cena():
            item = QStandardItem()
            item.setText(delivery.cognome + ", " + delivery.indirizzo + ", ore " + delivery.orario)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model_cena.appendRow(item)
        self.lista_cena.setModel(self.list_view_model_cena)

    def mostra_delivery(self):
        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare un ordine!")
        else:
            selected = self.lista.selectedIndexes()[0].row()
            delivery_selezionato = self.ldc.get_delivery(selected)
            print(delivery_selezionato)
            self.dv = delivery_view(delivery_selezionato, self.ldc.remove_delivery, self.genera_lista, self.genera_lista_cena, "pranzo")
            self.dv.show()

    def mostra_delivery_cena(self):
        if not self.lista_cena.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare un ordine!")
        else:
            selected_ = self.lista_cena.selectedIndexes()[0].row()
            delivery_selezionato_ = self.ldc.get_delivery_cena(selected_)
            self.dv = delivery_view(delivery_selezionato_, self.ldc.remove_delivery_cena, self.genera_lista, self.genera_lista_cena, "cena")
            self.dv.show()

    def cancel(self):
        self.ldc.cancel()
        self.ldc.cancel_cena()
        self.ldc.save_data()
        self.genera_lista()
        self.genera_lista_cena()
        QMessageBox.information(None, "RGest", "Tutti gli ordini delivery sono stati cancellati!")

    def newelement(self):
        self.closeEvent(self.ldc.save_data())
        self.ipv = inserisci_delivery_view(self.ldc, self.genera_lista, self.genera_lista_cena)
        self.ipv.show()

    def termina(self):
        n = 0
        for delivery in self.ldc.get_lista_delivery():
            n += 1
        #self.lcc.aggiungi_coperto(coperti_model(n))
        for delivery in self.ldc.get_lista_delivery():
            '''if self.controllo(cliente_model(delivery.cognome, delivery.telefono)):
                pass
            else:'''
            self.lclientic.aggiungi_cliente(cliente_model(delivery.cognome, delivery.telefono))
        for delivery in self.ldc.get_lista_delivery_cena():
            n += 1
        # aggiungi i delivery della giornata attraverso il controller
        self.lcopertic.aggiungi_consegna(consegna_delivery_model(n))
        for delivery in self.ldc.get_lista_delivery_cena():
            '''if self.controllo(cliente_model(delivery.cognome, delivery.telefono)):
                pass
            else:'''
            self.lclientic.aggiungi_cliente(cliente_model(delivery.cognome, delivery.telefono))
        self.ldc.cancel()
        self.ldc.cancel_cena()
        self.genera_lista()
        self.genera_lista_cena()
        QMessageBox.information(None, "RGest", "Giornata terminata! Il numero degli ordini delivery e i contatti dei "
                                               "clienti sono stati salvati correttamente!")
        self.close()

    def controllo(self, c):
        for cliente in self.lclientic.get_lista_clienti():
            if c.nome == cliente.nome and c.telefono == cliente.telefono:
                return True
        return False

    def closeEvent(self, event):
        self.ldc.save_data()
        self.lcopertic.save_data_delivery()
        self.lclientic.save_data()
