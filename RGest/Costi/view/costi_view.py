from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTableWidget, QPushButton, QWidget, QBoxLayout, QListView, \
    QVBoxLayout, QGridLayout, QTableWidgetItem

from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller
from Lista_tasse.controller.lista_tasse_controller import lista_tasse_controller


class costi_view(QMainWindow):

    def __init__(self):
        super(costi_view, self).__init__()

        self.ldc = lista_dipendenti_controller()
        self.lccc = lista_costi_covid_controller()
        self.ltc = lista_tasse_controller()

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
        self.tab_widget.addTab(self.tab1, "Dipendenti")
        self.tab_widget.addTab(self.tab2, "Costi covid")
        self.tab_widget.addTab(self.tab3, "Tasse")

        self.lista = QTableWidget()
        self.totale = QTableWidget()
        # self.totale.setFixedSize(726, 25)
        self.lista.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista()

        self.lista_covid = QTableWidget()
        self.totale_covid = QTableWidget()
        # self.totale_covid.setFixedSize(726, 25)
        self.lista_covid.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale_covid.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista_covid()

        self.lista_tasse = QTableWidget()
        self.totale_tasse = QTableWidget()
        # self.totale_tasse.setFixedSize(726, 25)
        self.lista_tasse.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale_tasse.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista_tasse()

        layout1 = QGridLayout(self)
        layout1.addWidget(self.lista, 0, 0)
        layout1.addWidget(self.totale, 1, 0)
        self.tab1.setLayout(layout1)

        layout2 = QGridLayout(self)
        layout2.addWidget(self.lista_covid, 0, 0)
        layout2.addWidget(self.totale_covid, 1, 0)
        self.tab2.setLayout(layout2)

        layout3 = QGridLayout(self)
        layout3.addWidget(self.lista_tasse, 0, 0)
        layout3.addWidget(self.totale_tasse, 1, 0)
        self.tab3.setLayout(layout3)

    def genera_lista(self):
        tot = 0
        a = 0
        self.lista.setColumnCount(3)
        self.totale.setColumnCount(2)
        self.totale.setRowCount(1)
        self.totale.setEnabled(False)
        self.lista.setHorizontalHeaderLabels(["Nominativo", "Ruolo", "Stipendio"])
        self.totale.setHorizontalHeaderLabels(["Totale", "Importo"])
        for row, date in enumerate(self.ldc.get_lista_dipendenti()):
            a += 1
            self.lista.setRowCount(a)
            item = QTableWidgetItem(date.nome)
            item2 = QTableWidgetItem(date.ruolo)
            item3 = QTableWidgetItem("€" + str(date.stipendio))
            self.lista.setItem(row, 0, item)
            self.lista.setItem(row, 1, item2)
            self.lista.setItem(row, 2, item3)
            tot += int(date.stipendio)
        self.totale.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale.setItem(0, 1, QTableWidgetItem("€" + str(tot)))
        '''self.list_view_model = QStandardItemModel(self.lista)
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
        self.totale.setModel(self.totale_view_model)'''

    def genera_lista_covid(self):
        tot = 0
        # self.list_covid_view_model = QStandardItemModel(self.lista_covid)
        # self.lccc.cancel()
        # self.lccc.save_data()
        a = 0
        self.lista_covid.setColumnCount(7)
        self.totale_covid.setColumnCount(2)
        self.totale_covid.setRowCount(1)
        self.totale_covid.setEnabled(False)
        self.lista_covid.setHorizontalHeaderLabels(["Mascherine", "Gel", "Guanti", "Igienizzante", "Disinfestazione",
                                                    "Data", "Totale"])
        self.totale_covid.setHorizontalHeaderLabels(["Totale", "Importo"])
        for row, date in enumerate(self.lccc.get_lista_covid()):
            a += 1
            self.lista_covid.setRowCount(a)
            item = QTableWidgetItem("€" + str(date.mascherine))
            item2 = QTableWidgetItem("€" + str(date.gel))
            item3 = QTableWidgetItem("€" + str(date.guanti))
            item4 = QTableWidgetItem("€" + str(date.igienizzanti))
            item5 = QTableWidgetItem("€" + str(date.disinfestazione))
            item6 = QTableWidgetItem(date.data)
            item7 = QTableWidgetItem("€" + str(date.totale))
            self.lista_covid.setItem(row, 0, item)
            self.lista_covid.setItem(row, 1, item2)
            self.lista_covid.setItem(row, 2, item3)
            self.lista_covid.setItem(row, 3, item4)
            self.lista_covid.setItem(row, 4, item5)
            self.lista_covid.setItem(row, 5, item6)
            self.lista_covid.setItem(row, 6, item7)
            tot += date.totale
        self.totale_covid.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale_covid.setItem(0, 1, QTableWidgetItem("€" + str(tot)))
        '''for ordine in self.lccc.get_lista_covid():
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
        self.totale_covid.setModel(self.totale_covid_view_model)'''

    def genera_lista_tasse(self):
        tot1 = 0
        tot2 = 0
        tot3 = 0
        tot4 = 0
        tot5 = 0
        a = 0
        # self.list_tax_view_model = QStandardItemModel(self.lista_tasse)
        # self.ltc.cancel()
        # self.ltc.save_data()
        self.lista_tasse.setColumnCount(6)
        self.totale_tasse.setColumnCount(1)
        self.totale_tasse.setRowCount(6)
        self.totale_tasse.setEnabled(False)
        self.lista_tasse.setHorizontalHeaderLabels(["Acqua", "Luce", "Gas", "Tv", "Affitto",
                                                    "Data"])
        self.totale_tasse.setHorizontalHeaderLabels(["Importo"])
        self.totale_tasse.setVerticalHeaderLabels(["Acqua", "Luce", "Gas", "Tv", "Affitto",
                                                   "Totale"])
        for row, date in enumerate(self.ltc.get_lista_tasse()):
            a += 1
            self.lista_tasse.setRowCount(a)
            item = QTableWidgetItem("€" + str(date.acqua))
            item2 = QTableWidgetItem("€" + str(date.luce))
            item3 = QTableWidgetItem("€" + str(date.gas))
            item4 = QTableWidgetItem("€" + str(date.tv))
            item5 = QTableWidgetItem("€" + str(date.affitto))
            item6 = QTableWidgetItem(date.data)
            self.lista_tasse.setItem(row, 0, item)
            self.lista_tasse.setItem(row, 1, item2)
            self.lista_tasse.setItem(row, 2, item3)
            self.lista_tasse.setItem(row, 3, item4)
            self.lista_tasse.setItem(row, 4, item5)
            self.lista_tasse.setItem(row, 5, item6)
            tot1 += int(date.acqua)
            tot2 += int(date.luce)
            tot3 += int(date.gas)
            tot4 += int(date.tv)
            tot5 += int(date.affitto)
        tot = [tot1, tot2, tot3, tot4, tot5]
        self.totale_tasse.setItem(0, 0, QTableWidgetItem("€" + str(tot1)))
        self.totale_tasse.setItem(1, 0, QTableWidgetItem("€" + str(tot2)))
        self.totale_tasse.setItem(2, 0, QTableWidgetItem("€" + str(tot3)))
        self.totale_tasse.setItem(3, 0, QTableWidgetItem("€" + str(tot4)))
        self.totale_tasse.setItem(4, 0, QTableWidgetItem("€" + str(tot5)))
        self.totale_tasse.setItem(5, 0, QTableWidgetItem("€" + str(sum(tot))))
        '''for tax in self.ltc.get_lista_tasse():
            item = QStandardItem()
            item.setText(self.stringa(tax.data, tax.acqua, tax.luce, tax.gas, tax.tv, tax.affitto))
            item.setEditable(False)
            item.setEnabled(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_tax_view_model.appendRow(item)
            tot1 += int(tax.acqua)
            tot2 += int(tax.luce)
            tot3 += int(tax.gas)
            tot4 += int(tax.tv)
            tot5 += int(tax.affitto)
        self.lista_tasse.setModel(self.list_tax_view_model)
        self.totale_tasse_view_model = QStandardItemModel(self.totale_tasse)
        itemTotale = QStandardItem()
        itemTotale.setText(
            "Totale     Acqua: €" + str(tot1) + ", luce: €" + str(tot2) + ", gas: €" + str(tot3) + ", tv: €" + str(
                tot4) + ", affitto: €" + str(tot5))
        print(3)
        itemTotale.setEditable(False)
        itemTotale.setEnabled(False)
        itemTotale.setFont(QFont("Times Roman", 11, QFont.Bold))
        self.totale_tasse_view_model.appendRow(itemTotale)
        self.totale_tasse.setModel(self.totale_tasse_view_model)

    def stringa(self, a, b, c, d, e, f):
        return a + " Acqua: €" + b + ", luce: €" + c + ", gas: €" + d + ", tv: €" + e + ", affitto: €" + f
'''
    # def closeEvent(self, event):
    #   self.ldc.save_data()
    #  self.lccc.save_data()
