from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QListView, QPushButton, QLabel, QMessageBox

from Lista_ordiniMP.controller.lista_ordiniMP_controller import lista_ordiniMP_controller
from Lista_ordiniMP.view.inserisci_ordineMP_view import inserisci_ordineMP_view


class lista_ordiniMP_view(QMainWindow):

    def __init__(self, lingua):
        super(lista_ordiniMP_view, self).__init__()

        self.lingua = lingua

        self.lordiniMPc = lista_ordiniMP_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QListView(self)

        self.aggiungi = QPushButton(self)
        self.visualizza = QPushButton(self)

        self.lista_label = QLabel(self)

        self.schermata()

    def schermata(self):

        global str1_, str2_, str3_
        if self.lingua == "Inglese":
            str1_ = "List of raw material orders to be confirmed"
            str2_ = "Add"
            str3_ = "View"
        if self.lingua == "Italiano":
            str1_ = "Elenco degli ordini materie prime da confermare"
            str2_ = "Aggiungi"
            str3_ = "Visualizza"

        font = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lista.move(125, 100)
        self.lista.setFixedSize(500, 400)

        self.lista_label.setText(str1_)
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(45, 40)
        self.lista_label.setFixedSize(660, 40)

        self.config_button(self.aggiungi, str2_, font, 150, 30, 200, 550)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.visualizza, str3_, font, 150, 30, 400, 550)
        self.visualizza.clicked.connect(self.mostra)

    def genera_lista(self):

        global str1, str2
        if self.lingua == "Inglese":
            str1 = "Order number "
            str2 = " elements"
        if self.lingua == "Italiano":
            str1 = "Ordine numero "
            str2 = " elementi"

        self.list_view_model = QStandardItemModel(self.lista)
        n = 1
        for ordine in self.lordiniMPc.get_lista_ordiniMP():
            item = QStandardItem()
            item.setText(str1 + str(n) + ", " + str(ordine.numero) + str2)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
            n += 1
        self.lista.setModel(self.list_view_model)

    def apri_inserimento(self):
        self.newelement()

    def newelement(self):
        self.closeEvent(self.lordiniMPc.save_data())
        self.icv = inserisci_ordineMP_view(self.lordiniMPc, self.genera_lista, [], True, self.lingua)
        self.icv.show()

    def mostra(self):

        global str11
        if self.lingua == "Inglese":
            str11 = "Select an order!"
        if self.lingua == "Italiano":
            str11 = "Selezionare un ordine!"

        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", str11)
        else:
            selected = self.lista.selectedIndexes()[0].row()
            ordineMP_selected = self.lordiniMPc.get_ordineMP(selected)
            self.ioMPv = inserisci_ordineMP_view(self.lordiniMPc, self.genera_lista, ordineMP_selected.mp_list, False,
                                                 self.lingua, ordineMP_selected)
            self.ioMPv.show()

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def closeEvent(self, event):
        self.lordiniMPc.save_data()
