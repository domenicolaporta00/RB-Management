from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTableWidget, QPushButton, QWidget, QBoxLayout, QListView, \
    QVBoxLayout

from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller


class costi_view(QMainWindow):

    def __init__(self):
        super(costi_view, self).__init__()

        self.ldc = lista_dipendenti_controller()
        self.lccc = lista_costi_covid_controller()
        # aggiungere la lista delle tasse

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.tab_widget = QTabWidget(self)
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11)

        self.tab_widget.setFixedSize(500, 400)
        self.tab_widget.move(125, 100)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, "Dipendenti")
        self.tab_widget.addTab(self.tab2, "Costi covid")

        self.lista = QListView()
        self.totale = QListView()
        self.totale.setFixedSize(476, 25)
        self.lista.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista()

        self.lista_covid = QListView()
        self.totale_covid = QListView()
        self.totale_covid.setFixedSize(476, 25)
        self.lista_covid.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale_covid.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista_covid()

        layout1 = QVBoxLayout(self)
        layout1.addWidget(self.lista)
        layout1.addWidget(self.totale)
        self.tab1.setLayout(layout1)

        layout2 = QVBoxLayout(self)
        layout2.addWidget(self.lista_covid)
        layout2.addWidget(self.totale_covid)
        self.tab2.setLayout(layout2)

    def genera_lista(self):
        tot = 0
        self.list_view_model = QStandardItemModel(self.lista)
        for dipendente in self.ldc.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.ruolo + " €" + dipendente.stipendio)
            item.setEditable(False)
            item.setEnabled(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
            tot += int(dipendente.stipendio)
        self.lista.setModel(self.list_view_model)
        self.totale_view_model = QStandardItemModel(self.totale)
        itemTotale = QStandardItem()
        itemTotale.setText("Totale     €" + str(tot))
        itemTotale.setEditable(False)
        itemTotale.setEnabled(False)
        itemTotale.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.totale_view_model.appendRow(itemTotale)
        self.totale.setModel(self.totale_view_model)

    def genera_lista_covid(self):
        tot = 0
        self.list_covid_view_model = QStandardItemModel(self.lista_covid)
        # self.lccc.cancel()
        # self.lccc.save_data()
        a = 1
        for ordine in self.lccc.get_lista_covid():
            item = QStandardItem()
            item.setText("Ordine " + str(a) + ": " + ordine.data + "     €" + str(ordine.totale))
            item.setEditable(False)
            item.setEnabled(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_covid_view_model.appendRow(item)
            tot += ordine.totale
            a = a + 1
        self.lista_covid.setModel(self.list_covid_view_model)
        self.totale_covid_view_model = QStandardItemModel(self.totale_covid)
        itemTotale = QStandardItem()
        itemTotale.setText("Totale     €" + str(tot))
        itemTotale.setEditable(False)
        itemTotale.setEnabled(False)
        itemTotale.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.totale_covid_view_model.appendRow(itemTotale)
        self.totale_covid.setModel(self.totale_covid_view_model)

    # def closeEvent(self, event):
    #   self.ldc.save_data()
    #  self.lccc.save_data()
