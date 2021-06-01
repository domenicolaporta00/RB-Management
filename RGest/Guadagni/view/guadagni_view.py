from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QListView, QVBoxLayout

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

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11)

        self.tab_widget.setFixedSize(750, 600)
        self.tab_widget.move(0, 0)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.tab1, "Coperti")
        self.tab_widget.addTab(self.tab2, "Ordini")

        self.lista = QListView()
        self.totale = QListView()
        self.totale.setFixedSize(726, 25)
        self.lista.setStyleSheet("color: rgb(0, 255, 0)")
        self.totale.setStyleSheet("color: rgb(0, 255, 0)")
        self.genera_lista()

        self.lista_ordini = QListView()
        self.totale_ordini = QListView()
        self.totale_ordini.setFixedSize(726, 25)
        self.lista_ordini.setStyleSheet("color: rgb(0, 255, 0)")
        self.totale_ordini.setStyleSheet("color: rgb(0, 255, 0)")
        self.genera_lista_ordini()

        layout1 = QVBoxLayout(self)
        layout1.addWidget(self.lista)
        layout1.addWidget(self.totale)
        self.tab1.setLayout(layout1)

        layout2 = QVBoxLayout(self)
        layout2.addWidget(self.lista_ordini)
        layout2.addWidget(self.totale_ordini)
        self.tab2.setLayout(layout2)

    def genera_lista(self):
        # self.lcc.cancel()
        # self.lcc.save_data()
        tot = 0
        self.list_view_model = QStandardItemModel(self.lista)
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
        self.totale.setModel(self.totale_view_model)

    def genera_lista_ordini(self):
        pass
