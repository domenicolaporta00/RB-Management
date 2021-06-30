from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTableWidget, QPushButton, QWidget, QBoxLayout, QListView, \
    QVBoxLayout, QGridLayout, QTableWidgetItem

from Lista_contiMP.controller.lista_contiMP_controller import lista_contiMP_controller
from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller
from Lista_tasse.controller.lista_tasse_controller import lista_tasse_controller


class costi_view(QMainWindow):

    def __init__(self):
        super(costi_view, self).__init__()

        self.ldc = lista_dipendenti_controller()
        self.lccc = lista_costi_covid_controller()
        self.ltc = lista_tasse_controller()
        self.lcMPc = lista_contiMP_controller()

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
        self.tab4 = QWidget(self)

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
        self.tab_widget.addTab(self.tab4, "Ordini materie prime")

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

        self.lista_costiMP = QTableWidget()
        self.totale_costiMP = QTableWidget()
        self.lista_costiMP.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale_costiMP.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista_costiMP()

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

        layout4 = QGridLayout(self)
        layout4.addWidget(self.lista_costiMP, 0, 0)
        layout4.addWidget(self.totale_costiMP, 1, 0)
        self.tab4.setLayout(layout4)

    def genera_lista(self):
        tot = 0
        a = 0
        self.lista.setColumnCount(4)
        self.totale.setColumnCount(2)
        self.totale.setRowCount(1)
        self.totale.setEnabled(False)
        self.lista.setColumnWidth(0, 100)
        self.lista.setColumnWidth(1, 150)
        self.lista.setColumnWidth(2, 100)
        self.lista.setColumnWidth(3, 175)
        self.lista.setHorizontalHeaderLabels(["Nominativo", "Ruolo", "Stipendio", "Data assunzione"])
        self.totale.setHorizontalHeaderLabels(["Totale", "Importo"])
        for row, date in enumerate(self.ldc.get_lista_dipendenti()):
            a += 1
            self.lista.setRowCount(a)
            item = QTableWidgetItem(date.nome)
            item2 = QTableWidgetItem(date.ruolo)
            item3 = QTableWidgetItem("€" + str(date.stipendio))
            item4 = QTableWidgetItem(date.data_inizio)
            self.lista.setItem(row, 0, item)
            self.lista.setItem(row, 1, item2)
            self.lista.setItem(row, 2, item3)
            self.lista.setItem(row, 3, item4)
            tot += int(date.stipendio)
        self.totale.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale.setItem(0, 1, QTableWidgetItem("€" + str(tot)))

    def genera_lista_covid(self):
        tot = 0
        a = 0
        self.lista_covid.setColumnCount(7)
        self.totale_covid.setColumnCount(2)
        self.totale_covid.setRowCount(1)
        self.totale_covid.setEnabled(False)
        self.lista_covid.setColumnWidth(1, 75)
        self.lista_covid.setColumnWidth(2, 75)
        self.lista_covid.setColumnWidth(5, 175)
        self.lista_covid.setColumnWidth(6, 75)
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

    def genera_lista_tasse(self):
        tot1 = 0
        tot2 = 0
        tot3 = 0
        tot4 = 0
        tot5 = 0
        a = 0
        self.lista_tasse.setColumnCount(6)
        self.totale_tasse.setColumnCount(1)
        self.totale_tasse.setRowCount(6)
        self.totale_tasse.setEnabled(False)
        self.lista_tasse.setColumnWidth(5, 175)
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

    def genera_lista_costiMP(self):
        self.lista_costiMP.setColumnCount(3)
        self.totale_costiMP.setColumnCount(2)
        self.totale_costiMP.setRowCount(1)
        self.lista_costiMP.setColumnWidth(1, 175)
        self.lista_costiMP.setColumnWidth(0, 75)
        self.totale_costiMP.setEnabled(False)
        self.lista_costiMP.setHorizontalHeaderLabels(["Orario", "Data", "Costo"])
        self.totale_costiMP.setHorizontalHeaderLabels(["Totale", "Importo"])
        a = 0
        tot = 0
        for row, date in enumerate(self.lcMPc.get_lista_contoMP()):
            a += 1
            self.lista_costiMP.setRowCount(a)
            item = QTableWidgetItem(date.orario)
            item2 = QTableWidgetItem(date.data)
            item3 = QTableWidgetItem("€" + str(date.conto))
            self.lista_costiMP.setItem(row, 0, item)
            self.lista_costiMP.setItem(row, 1, item2)
            self.lista_costiMP.setItem(row, 2, item3)
            tot += date.conto
        self.totale_costiMP.setItem(0, 0, QTableWidgetItem("Totale"))
        self.totale_costiMP.setItem(0, 1, QTableWidgetItem("€" + str(tot)))
