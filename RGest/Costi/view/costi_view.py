from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTableWidget, QWidget, QGridLayout, QTableWidgetItem

from Lista_contiMP.controller.lista_contiMP_controller import lista_contiMP_controller
from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller
from Lista_tasse.controller.lista_tasse_controller import lista_tasse_controller


class costi_view(QMainWindow):

    def __init__(self, lingua):
        super(costi_view, self).__init__()

        self.lingua = lingua

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

        '''self.lccc.cancel()
        self.lccc.save_data()
        self.ltc.cancel()
        self.ltc.save_data()
        self.lcMPc.cancel_contoMP()
        self.lcMPc.save_data()'''

        global str2, str1, str3, str4
        if self.lingua == "Inglese":
            str1 = "Employees"
            str2 = "Covid costs"
            str3 = "Taxes"
            str4 = "Raw material orders"
        if self.lingua == "Italiano":
            str1 = "Dipendenti"
            str2 = "Costi covid"
            str3 = "Tasse"
            str4 = "Ordini materie prime"

        font = QFont("Times Roman", 11)

        self.tab_widget.setFixedSize(750, 600)
        self.tab_widget.move(0, 0)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, str1)
        self.tab_widget.addTab(self.tab2, str2)
        self.tab_widget.addTab(self.tab3, str3)
        self.tab_widget.addTab(self.tab4, str4)

        self.lista = QTableWidget()
        self.totale = QTableWidget()
        self.lista.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista()

        self.lista_covid = QTableWidget()
        self.totale_covid = QTableWidget()
        self.lista_covid.setStyleSheet("color: rgb(255, 0, 0)")
        self.totale_covid.setStyleSheet("color: rgb(255, 0, 0)")
        self.genera_lista_covid()

        self.lista_tasse = QTableWidget()
        self.totale_tasse = QTableWidget()
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

        global str2_, str1_, str3_, str4_, str5_, str6_
        if self.lingua == "Inglese":
            str1_ = "Name"
            str2_ = "Role"
            str3_ = "Salary"
            str4_ = "Assumption date"
            str5_ = "Total"
            str6_ = "Amount"
        if self.lingua == "Italiano":
            str1_ = "Nominativo"
            str2_ = "Ruolo"
            str3_ = "Stipendio"
            str4_ = "Data assunzione"
            str5_ = "Totale"
            str6_ = "Importo"

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
        self.lista.setHorizontalHeaderLabels([str1_, str2_, str3_, str4_])
        self.totale.setHorizontalHeaderLabels([str5_, str6_])
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
        self.totale.setItem(0, 0, QTableWidgetItem(str5_))
        self.totale.setItem(0, 1, QTableWidgetItem("€" + str(tot)))

    def genera_lista_covid(self):

        global _str2, _str1, _str3, _str4, _str5, _str6, _str7
        if self.lingua == "Inglese":
            _str1 = "Masks"
            _str2 = "Gloves"
            _str3 = "Sanitizing"
            _str4 = "Disinfestation"
            _str5 = "Total"
            _str6 = "Date"
            _str7 = "Amount"
        if self.lingua == "Italiano":
            _str1 = "Mascherine"
            _str2 = "Guanti"
            _str3 = "Igienizzante"
            _str4 = "Disinfestazione"
            _str5 = "Totale"
            _str6 = "Data"
            _str7 = "Importo"

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
        self.lista_covid.setHorizontalHeaderLabels([_str1, "Gel", _str2, _str3, _str4,
                                                    _str6, _str5])
        self.totale_covid.setHorizontalHeaderLabels([_str5, _str7])
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
        self.totale_covid.setItem(0, 0, QTableWidgetItem(_str5))
        self.totale_covid.setItem(0, 1, QTableWidgetItem("€" + str(tot)))

    def genera_lista_tasse(self):

        global str11, str21, str31, str41, str51, str61
        if self.lingua == "Inglese":
            str11 = "Water"
            str21 = "Electricity"
            str31 = "Rent"
            str41 = "Date"
            str51 = "Amount"
            str61 = "Total"
        if self.lingua == "Italiano":
            str11 = "Acqua"
            str21 = "Luce"
            str31 = "Affitto"
            str41 = "Data"
            str51 = "Importo"
            str61 = "Totale"

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
        self.lista_tasse.setHorizontalHeaderLabels([str11, str21, "Gas", "Tv", str31,
                                                    str41])
        self.totale_tasse.setHorizontalHeaderLabels([str51])
        self.totale_tasse.setVerticalHeaderLabels([str11, str21, "Gas", "Tv", str31,
                                                   str61])
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

        global str12, str22, str32, str42, str52, str62
        if self.lingua == "Inglese":
            str12 = "Time"
            str22 = "Date"
            str32 = "Cost"
            str52 = "Amount"
            str62 = "Total"
        if self.lingua == "Italiano":
            str12 = "Orario"
            str22 = "Data"
            str32 = "Costo"
            str52 = "Importo"
            str62 = "Totale"

        self.lista_costiMP.setColumnCount(3)
        self.totale_costiMP.setColumnCount(2)
        self.totale_costiMP.setRowCount(1)
        self.lista_costiMP.setColumnWidth(1, 175)
        self.lista_costiMP.setColumnWidth(0, 75)
        self.totale_costiMP.setEnabled(False)
        self.lista_costiMP.setHorizontalHeaderLabels([str12, str22, str32])
        self.totale_costiMP.setHorizontalHeaderLabels([str52, str62])
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
        self.totale_costiMP.setItem(0, 0, QTableWidgetItem(str62))
        self.totale_costiMP.setItem(0, 1, QTableWidgetItem("€" + str(tot)))
