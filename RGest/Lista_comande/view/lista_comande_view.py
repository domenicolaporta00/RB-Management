from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QMainWindow, QListView, QPushButton, QLabel, QMessageBox

from Lista_comande.controller.lista_comande_controller import lista_comande_controller
from Lista_comande.view.inserisci_comanda_view import inserisci_comanda_view
from Lista_materie_prime.controller.lista_materie_prime_controller import lista_materie_prime_controller


class lista_comande_view(QMainWindow):

    def __init__(self, isDelivery, lingua):
        super(lista_comande_view, self).__init__()

        self.lingua = lingua
        self.isDelivery = isDelivery

        self.lcomandec = lista_comande_controller()
        # self.lmatprimec = lista_materie_prime_controller()

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

        global str5, str4, str3, str2_
        if self.lingua == "Inglese":
            str2_ = "List of delivery orders"
            str3 = "List of orders at the table"
            str4 = "Add"
            str5 = "View"
        elif self.lingua == "Italiano":
            str2_ = "Elenco delle comande delivery"
            str3 = "Elenco delle comande a tavola"
            str4 = "Aggiungi"
            str5 = "Visualizza"

        font = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lista.move(125, 100)
        self.lista.setFixedSize(500, 400)

        if self.isDelivery:
            self.lista_label.setText(str2_)
        elif not self.isDelivery:
            self.lista_label.setText(str3)
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(170, 40)
        self.lista_label.setFixedSize(410, 40)

        self.config_button(self.aggiungi, str4, font, 150, 30, 200, 550)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.visualizza, str5, font, 150, 30, 400, 550)
        self.visualizza.clicked.connect(self.mostra)

    def genera_lista(self):
        global str2, str1
        if self.lingua == "Inglese":
            str1 = "Order number "
            str2 = " courses"
        if self.lingua == "Italiano":
            str1 = "Ordine numero "
            str2 = " piatti"
        self.list_view_model = QStandardItemModel(self.lista)
        n = 1
        for comanda in self.lcomandec.get_lista_comande():
            item = QStandardItem()
            item.setText(str1 + str(n) + ", " + str(comanda.numero) + str2)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
            n += 1
        self.lista.setModel(self.list_view_model)

    def apri_inserimento(self):
        self.newelement()

    def newelement(self):
        global str2, str1
        if self.lingua == "Inglese":
            str1 = "Empty warehouse! Impossible to order!"
            str2 = "Oil and/or salt not in warehouse! Impossible to order!"
        if self.lingua == "Italiano":
            str1 = "Magazzino vuoto! Impossibile ordinare!"
            str2 = "Olio e/o sale non presenti in magazzino! Impossibile ordinare!"
        if self.magazzinoVuoto():
            QMessageBox.warning(None, "RGest", str1)
        if not self.magazzinoVuoto():
            if not self.sale_olio():
                QMessageBox.warning(None, "RGest", str2)
            if self.sale_olio():
                self.closeEvent(self.lcomandec.save_data())
                self.icv = inserisci_comanda_view(self.lcomandec, self.genera_lista, [], True)
                self.icv.show()

    def mostra(self):
        global str1
        if self.lingua == "Inglese":
            str1 = "Select an order!"
        if self.lingua == "Italiano":
            str1 = "Selezionare un ordine!"
        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", str1)
        else:
            selected = self.lista.selectedIndexes()[0].row()
            ordine_selected = self.lcomandec.get_comanda(selected)
            self.vc = inserisci_comanda_view(self.lcomandec, self.genera_lista, ordine_selected.piatti_list, False,
                                             ordine_selected)
            self.vc.show()

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def magazzinoVuoto(self):
        self.lmatprimec = lista_materie_prime_controller()

        def quanti(matPrima):
            a = 0
            for mp in self.lmatprimec.get_lista_magazzino():
                if mp == (matPrima.nome, matPrima.prezzo):
                    a += 1
            return a

        for matPrima in self.lmatprimec.get_lista_mp():
            if quanti(matPrima) != 0:
                return False
        return True

    def sale_olio(self):
        self.lmatprimec = lista_materie_prime_controller()

        def quanti(matPrima):
            a = 0
            for mp in self.lmatprimec.get_lista_magazzino():
                if mp == (matPrima.nome, matPrima.prezzo):
                    a += 1
            return a

        if quanti(self.lmatprimec.get_mp(25)) == 0 or quanti(self.lmatprimec.get_mp(26)) == 0:
            return False
        return True

    def closeEvent(self, event):
        self.lcomandec.save_data()
