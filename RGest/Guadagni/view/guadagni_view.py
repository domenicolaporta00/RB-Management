from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QListView, QVBoxLayout, QTableWidget, QGridLayout, \
    QTableWidgetItem

from Lista_coperti.controller.lista_coperti_controller import lista_coperti_controller


class guadagni_view(QMainWindow):

    def __init__(self):
        super(guadagni_view, self).__init__()

        self.lcc = lista_coperti_controller()
        # controller dei guadagni

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
        font = QFont("Times Roman", 11)

        self.tab_widget.setFixedSize(750, 600)
        self.tab_widget.move(0, 0)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, "Coperti")
        self.tab_widget.addTab(self.tab2, "Ordini")
        self.tab_widget.addTab(self.tab3, "Consegne delivery")

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
        tot = 0
        '''self.list_view_model = QStandardItemModel(self.lista)
        for coperto in self.lcc.get_lista_coperti():
            item = QStandardItem()
            item.setText(coperto.data + " " + str(coperto.n) + " coperti. Ricavo: €" + str(coperto.ricavo_tot))
            item.setEditable(False)
            item.setEnabled(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
            tot += int(coperto.ricavo_tot)
        self.lista.setModel(self.list_view_model)
        self.totale_view_model = QStandardItemModel(self.totale)
        itemTotale = QStandardItem()
        itemTotale.setText("Totale     €" + str(tot))
        itemTotale.setEditable(False)
        itemTotale.setEnabled(False)
        itemTotale.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.totale_view_model.appendRow(itemTotale)
        self.totale.setModel(self.totale_view_model)'''
        self.lista.setColumnCount(3)
        self.totale.setColumnCount(2)
        self.totale.setRowCount(1)
        self.lista.setColumnWidth(0, 150)
        self.lista.setColumnWidth(1, 75)
        self.lista.setColumnWidth(2, 75)
        #self.lista.setColumnWidth(0, 75)
        self.totale.setEnabled(False)
        self.lista.setHorizontalHeaderLabels(["Data", "Coperti", "Ricavo"])
        self.totale.setHorizontalHeaderLabels(["Totale", "Importo"])
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
        self.totale.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale.setItem(0, 1, QTableWidgetItem("€" + str(tot)))

    def genera_lista_ordini(self):
        self.lista_ordini.setColumnCount(3)
        self.totale_ordini.setColumnCount(2)
        self.totale_ordini.setRowCount(1)
        self.lista_ordini.setColumnWidth(1, 150)
        self.lista_ordini.setColumnWidth(0, 75)
        self.totale_ordini.setEnabled(False)
        self.lista_ordini.setHorizontalHeaderLabels(["Orario", "Data", "Ricavo"])
        self.totale_ordini.setHorizontalHeaderLabels(["Totale", "Importo"])
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
        self.totale_ordini.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale_ordini.setItem(0, 1, QTableWidgetItem("€"+str(tot)))

    def genera_lista_delivery(self):
        self.lista_delivery.setColumnCount(3)
        self.totale_delivery.setColumnCount(2)
        self.totale_delivery.setRowCount(1)
        self.lista_delivery.setColumnWidth(0, 150)
        self.lista_delivery.setColumnWidth(1, 75)
        self.lista_delivery.setColumnWidth(2, 75)
        self.totale_delivery.setEnabled(False)
        self.lista_delivery.setHorizontalHeaderLabels(["Data", "Consegne", "Ricavo"])
        self.totale_delivery.setHorizontalHeaderLabels(["Totale", "Importo"])
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
        self.totale_delivery.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale_delivery.setItem(0, 1, QTableWidgetItem("€" + str(tot)))



