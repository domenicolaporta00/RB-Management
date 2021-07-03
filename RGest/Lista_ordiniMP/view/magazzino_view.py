from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QLabel

from Lista_materie_prime.controller.lista_materie_prime_controller import lista_materie_prime_controller


class magazzino_view(QMainWindow):

    def __init__(self, lingua):
        super(magazzino_view, self).__init__()

        self.lingua = lingua

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lmatprimec = lista_materie_prime_controller()

        self.label = QLabel(self)

        self.table_widget = QTableWidget(self)

        self.schermata()

    def schermata(self):

        global str11
        if self.lingua == "Inglese":
            str11 = "Warehouse"
        if self.lingua == "Italiano":
            str11 = "Magazzino"

        font = QFont("Times Roman", 20, QFont.Bold)

        self.config_label(self.label, str11, 300, 40, 160, 40, font)

        self.genera_lista()

    def quanti(self, matPrima):
        a = 0
        for mp in self.lmatprimec.get_lista_magazzino():
            if mp == (matPrima.nome, matPrima.prezzo):
                a += 1
        return a

    def genera_lista(self):

        global str1, str2, str3
        if self.lingua == "Inglese":
            str1 = "Product"
            str2 = "Quantity"
            str3 = "Unit price"
        if self.lingua == "Italiano":
            str1 = "Prodotto"
            str2 = "Quantità"
            str3 = "Prezzo unitario"

        self.table_widget.move(129, 100)
        self.table_widget.setFixedSize(492, 400)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels([str1, str2, str3])
        self.table_widget.setColumnWidth(0, 250)
        self.table_widget.setColumnWidth(1, 100)
        self.table_widget.setColumnWidth(2, 100)
        a = 0
        for row, matPrima in enumerate(self.lmatprimec.get_lista_mp()):
            a += 1
            self.table_widget.setRowCount(a)
            item = QTableWidgetItem(matPrima.nome)
            item2 = QTableWidgetItem(str(self.quanti(matPrima)))
            item3 = QTableWidgetItem("€" + str(matPrima.prezzo))
            self.table_widget.setItem(row, 0, item)
            self.table_widget.setItem(row, 1, item2)
            self.table_widget.setItem(row, 2, item3)

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)
