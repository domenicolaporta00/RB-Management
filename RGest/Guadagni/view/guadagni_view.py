from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QListView, QVBoxLayout, QTableWidget, QGridLayout, \
    QTableWidgetItem

from Lista_coperti.controller.lista_coperti_controller import lista_coperti_controller


class guadagni_view(QMainWindow):

    def __init__(self, lingua):
        super(guadagni_view, self).__init__()

        self.lingua = lingua

        self.lcc = lista_coperti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.tab_widget = QTabWidget(self)
        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)
        self.tab3 = QWidget(self)

        self.schermata()

    def schermata(self):

        global str2, str1, str3
        if self.lingua == "Inglese":
            str1 = "Place settings"
            str2 = "Orders"
            str3 = "Home delivery"
        if self.lingua == "Italiano":
            str1 = "Coperti"
            str2 = "Ordini"
            str3 = "Consegne delivery"

        font = QFont("Times Roman", 11)

        self.tab_widget.setFixedSize(750, 600)
        self.tab_widget.move(0, 0)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, str1)
        self.tab_widget.addTab(self.tab2, str2)
        self.tab_widget.addTab(self.tab3, str3)

        self.lista = QTableWidget()
        self.totale = QTableWidget()
        #self.totale.setFixedSize(726, 25)
        self.lista.setStyleSheet("color: rgb(0, 255, 0)")
        self.totale.setStyleSheet("color: rgb(0, 255, 0)")
        self.genera_lista()

        self.lista_ordini = QTableWidget()
        self.totale_ordini = QTableWidget()
        self.lista_ordini.setStyleSheet("color: rgb(0, 255, 0)")
        self.totale_ordini.setStyleSheet("color: rgb(0, 255, 0)")
        self.genera_lista_ordini()

        self.lista_delivery = QTableWidget()
        self.totale_delivery = QTableWidget()
        self.lista_delivery.setStyleSheet("color: rgb(0, 255, 0)")
        self.totale_delivery.setStyleSheet("color: rgb(0, 255, 0)")
        self.genera_lista_delivery()

        layout1 = QGridLayout(self)
        layout1.addWidget(self.lista, 0, 0)
        layout1.addWidget(self.totale, 0, 1)
        self.tab1.setLayout(layout1)

        layout2 = QGridLayout(self)
        layout2.addWidget(self.lista_ordini, 0, 0)
        layout2.addWidget(self.totale_ordini, 0, 1)
        self.tab2.setLayout(layout2)

        layout3 = QGridLayout(self)
        layout3.addWidget(self.lista_delivery, 0, 0)
        layout3.addWidget(self.totale_delivery, 0, 1)
        self.tab3.setLayout(layout3)

    def genera_lista(self):
        # self.lcc.cancel()
        # self.lcc.save_data()

        global str21, str11, str31, str51, str61
        if self.lingua == "Inglese":
            str11 = "Date"
            str21 = "Place settings"
            str31 = "Proceeds"
            str51 = "Total"
            str61 = "Amount"
        if self.lingua == "Italiano":
            str11 = "Data"
            str21 = "Coperti"
            str31 = "Ricavo"
            str51 = "Totale"
            str61 = "Importo"

        tot = 0
        self.lista.setColumnCount(3)
        self.totale.setColumnCount(2)
        self.totale.setRowCount(1)
        self.lista.setColumnWidth(0, 150)
        self.lista.setColumnWidth(1, 75)
        self.lista.setColumnWidth(2, 75)
        #self.lista.setColumnWidth(0, 75)
        self.totale.setEnabled(False)
        self.lista.setHorizontalHeaderLabels([str11, str21, str31])
        self.totale.setHorizontalHeaderLabels([str51, str61])
        a = 0
        tot = 0
        for row, date in enumerate(self.lcc.get_lista_coperti()):
            a += 1
            self.lista.setRowCount(a)
            item = QTableWidgetItem(date.data)
            item2 = QTableWidgetItem(str(date.n))
            item3 = QTableWidgetItem("€" + str(date.ricavo_tot))
            self.lista.setItem(row, 0, item)
            self.lista.setItem(row, 1, item2)
            self.lista.setItem(row, 2, item3)
            tot += date.ricavo_tot
        self.totale.setItem(0, 0, QTableWidgetItem(str51))
        self.totale.setItem(0, 1, QTableWidgetItem("€" + str(tot)))

    def genera_lista_ordini(self):

        global str22, str12, str32, str52, str62
        if self.lingua == "Inglese":
            str12 = "Date"
            str22 = "Time"
            str32 = "Proceeds"
            str52 = "Total"
            str62 = "Amount"
        if self.lingua == "Italiano":
            str12 = "Data"
            str22 = "Orario"
            str32 = "Ricavo"
            str52 = "Totale"
            str62 = "Importo"

        self.lista_ordini.setColumnCount(3)
        self.totale_ordini.setColumnCount(2)
        self.totale_ordini.setRowCount(1)
        self.lista_ordini.setColumnWidth(1, 150)
        self.lista_ordini.setColumnWidth(0, 75)
        self.totale_ordini.setEnabled(False)
        self.lista_ordini.setHorizontalHeaderLabels([str22, str12, str32])
        self.totale_ordini.setHorizontalHeaderLabels([str52, str62])
        a = 0
        tot = 0
        for row, date in enumerate(self.lcc.get_lista_conto()):
            a += 1
            self.lista_ordini.setRowCount(a)
            item = QTableWidgetItem(date.orario)
            item2 = QTableWidgetItem(date.data)
            item3 = QTableWidgetItem("€"+str(date.conto))
            self.lista_ordini.setItem(row, 0, item)
            self.lista_ordini.setItem(row, 1, item2)
            self.lista_ordini.setItem(row, 2, item3)
            tot += date.conto
        self.totale_ordini.setItem(0, 0, QTableWidgetItem(str52))
        self.totale_ordini.setItem(0, 1, QTableWidgetItem("€"+str(tot)))

    def genera_lista_delivery(self):

        global str23, str13, str33, str53, str63
        if self.lingua == "Inglese":
            str13 = "Date"
            str23 = "Deliveries"
            str33 = "Proceeds"
            str53 = "Total"
            str63 = "Amount"
        if self.lingua == "Italiano":
            str13 = "Data"
            str23 = "Consegne"
            str33 = "Ricavo"
            str53 = "Totale"
            str63 = "Importo"

        self.lista_delivery.setColumnCount(3)
        self.totale_delivery.setColumnCount(2)
        self.totale_delivery.setRowCount(1)
        self.lista_delivery.setColumnWidth(0, 150)
        self.lista_delivery.setColumnWidth(1, 75)
        self.lista_delivery.setColumnWidth(2, 75)
        self.totale_delivery.setEnabled(False)
        self.lista_delivery.setHorizontalHeaderLabels([str13, str23, str33])
        self.totale_delivery.setHorizontalHeaderLabels([str53, str63])
        a = 0
        tot = 0
        for row, date in enumerate(self.lcc.get_lista_consegne_delivery()):
            a += 1
            self.lista_delivery.setRowCount(a)
            item = QTableWidgetItem(date.data)
            item2 = QTableWidgetItem(str(date.n))
            item3 = QTableWidgetItem("€"+str(date.ricavo_tot))
            self.lista_delivery.setItem(row, 0, item)
            self.lista_delivery.setItem(row, 1, item2)
            self.lista_delivery.setItem(row, 2, item3)
            tot += date.ricavo_tot
        self.totale_delivery.setItem(0, 0, QTableWidgetItem(str53))
        self.totale_delivery.setItem(0, 1, QTableWidgetItem("€" + str(tot)))



