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

        global str6, str5, str7, str4, str3, str1, str2
        if self.lingua == "Inglese":
            str1 = "Lunch"
            str2 = "Dinner"
            str3 = "Delivery list"
            str4 = "Modification"
            str5 = "Add"
            str6 = "Ends the day"
            str7 = "Delete everything"
        elif self.lingua == "Italiano":
            str1 = "Pranzo"
            str2 = "Cena"
            str3 = "Elenco delivery"
            str4 = "Modifica"
            str5 = "Aggiungi"
            str6 = "Termina giornata"
            str7 = "Elimina tutto"

        font = QFont("Times Roman", 11, QFont.Bold)

        self.tab_widget.setFixedSize(700, 450)
        self.tab_widget.move(25, 75)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, str1)
        self.tab_widget.addTab(self.tab2, str2)

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

        self.lista_label.setText(str3)
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(250, 40)
        self.lista_label.setFixedSize(250, 40)

        self.config_button(self.visualizza, str4, font, 150, 30, 36, 550)
        self.visualizza.clicked.connect(self.mostra_delivery)
        self.config_button(self.visualizza_cena, str4, font, 150, 30, 36, 550)
        self.visualizza_cena.clicked.connect(self.mostra_delivery_cena)
        self.config_button(self.aggiungi, str5, font, 150, 30, 211, 482)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.elimina, str7, font, 150, 30, 387, 482)
        self.elimina.clicked.connect(self.cancel)
        self.config_button(self.salva, str6, font, 150, 30, 562, 482)
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

        global str11
        if self.lingua == "Inglese":
            str11 = ", "
        if self.lingua == "Italiano":
            str11 = ", ore "

        self.list_view_model = QStandardItemModel(self.lista)
        for delivery in self.ldc.get_lista_delivery():
            item = QStandardItem()
            item.setText(delivery.cognome + ", " + delivery.indirizzo + str11 + delivery.orario)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
        self.lista.setModel(self.list_view_model)

    def genera_lista_cena(self):

        global str12
        if self.lingua == "Inglese":
            str12 = ", "
        if self.lingua == "Italiano":
            str12 = ", ore "

        self.list_view_model_cena = QStandardItemModel(self.lista_cena)
        for delivery in self.ldc.get_lista_delivery_cena():
            item = QStandardItem()
            item.setText(delivery.cognome + ", " + delivery.indirizzo + str12 + delivery.orario)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model_cena.appendRow(item)
        self.lista_cena.setModel(self.list_view_model_cena)

    def mostra_delivery(self):

        global str13
        if self.lingua == "Inglese":
            str13 = "Select an order!"
        if self.lingua == "Italiano":
            str13 = "Selezionare un ordine!"

        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", str13)
        else:
            selected = self.lista.selectedIndexes()[0].row()
            delivery_selezionato = self.ldc.get_delivery(selected)
            self.dv = delivery_view(delivery_selezionato, self.ldc.remove_delivery, self.genera_lista, self.genera_lista_cena, "pranzo", self.lingua)
            self.dv.show()

    def mostra_delivery_cena(self):

        global str14
        if self.lingua == "Inglese":
            str14 = "Select an order!"
        if self.lingua == "Italiano":
            str14 = "Selezionare un ordine!"

        if not self.lista_cena.selectedIndexes():
            QMessageBox.warning(None, "RGest", str14)
        else:
            selected_ = self.lista_cena.selectedIndexes()[0].row()
            delivery_selezionato_ = self.ldc.get_delivery_cena(selected_)
            self.dv = delivery_view(delivery_selezionato_, self.ldc.remove_delivery_cena, self.genera_lista, self.genera_lista_cena, "cena", self.lingua)
            self.dv.show()

    def cancel(self):

        global str15
        if self.lingua == "Inglese":
            str15 = "All delivery orders have been canceled!"
        if self.lingua == "Italiano":
            str15 = "Tutti gli ordini delivery sono stati cancellati!"

        self.ldc.cancel()
        self.ldc.cancel_cena()
        self.ldc.save_data()
        self.genera_lista()
        self.genera_lista_cena()
        QMessageBox.information(None, "RGest", str15)

    def newelement(self):
        self.closeEvent(self.ldc.save_data())
        self.ipv = inserisci_delivery_view(self.ldc, self.genera_lista, self.genera_lista_cena, self.lingua)
        self.ipv.show()

    def termina(self):

        global str16
        if self.lingua == "Inglese":
            str16 = "Day over! The number of delivery orders and customer contacts have been successfully saved!"
        if self.lingua == "Italiano":
            str16 = "Giornata terminata! Il numero degli ordini delivery e i contatti dei clienti sono stati salvati " \
                   "correttamente! "

        n = 0
        for delivery in self.ldc.get_lista_delivery():
            n += 1
        for delivery in self.ldc.get_lista_delivery():
            self.lclientic.aggiungi_cliente(cliente_model(delivery.cognome, delivery.telefono))
        for delivery in self.ldc.get_lista_delivery_cena():
            n += 1
        self.lcopertic.aggiungi_consegna(consegna_delivery_model(n))
        for delivery in self.ldc.get_lista_delivery_cena():
            self.lclientic.aggiungi_cliente(cliente_model(delivery.cognome, delivery.telefono))
        self.ldc.cancel()
        self.ldc.cancel_cena()
        self.genera_lista()
        self.genera_lista_cena()
        QMessageBox.information(None, "RGest", str16)
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
