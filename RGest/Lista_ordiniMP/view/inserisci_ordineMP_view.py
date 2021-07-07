import winsound

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QPushButton, QTabWidget, QWidget, QComboBox, QTableWidgetItem, \
    QMessageBox, QGridLayout

from ContoMP.model.contoMP_model import contoMP_model
from Lista_contiMP.controller.lista_contiMP_controller import lista_contiMP_controller
from Lista_materie_prime.controller.lista_materie_prime_controller import lista_materie_prime_controller
from OrdineMP.controller.ordineMP_controller import ordineMP_controller
from OrdineMP.model.ordineMP_model import ordineMP_model


class inserisci_ordineMP_view(QMainWindow):

    def __init__(self, controller, callback, elenco, isNuovo, lingua, ordine=None):
        super(inserisci_ordineMP_view, self).__init__()

        self.lingua = lingua

        self.matprime_ordine = elenco
        self.controller = controller
        self.callback = callback
        self.jsonobject = {}
        self.isNuovo = isNuovo
        self.ordine = ordine
        self.contr = ordineMP_controller(ordine)

        self.lmatprimec = lista_materie_prime_controller()
        self.lcMPc = lista_contiMP_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QTableWidget(self)
        self.lista_totale = QTableWidget(self)

        self.ok = QPushButton(self)
        self.aggiungi = QPushButton(self)
        self.cancel = QPushButton(self)
        self.paga = QPushButton(self)

        self.tab_widget = QTabWidget(self)
        self.widget = QWidget(self)
        self.tutto = QWidget(self)

        self.cb = QComboBox(self)

        self.schermata()

    def schermata(self):

        global str1, str2, str3, str4, str5, str6, str7
        if self.lingua == "Inglese":
            str1 = "Confirm"
            str2 = "Close order"
            str3 = "Delete"
            str4 = "Add"
            str5 = "Modification"
            str6 = "Order"
            str7 = "Total"
        if self.lingua == "Italiano":
            str1 = "Conferma"
            str2 = "Chiudi ordine"
            str3 = "Elimina"
            str4 = "Aggiungi"
            str5 = "Modifica"
            str6 = "Ordine"
            str7 = "Totale"

        font = QFont("Times Roman", 11)
        f = QFont("Times Roman", 11, QFont.Bold)

        if self.isNuovo:
            self.config_button(self.ok, str1, f, 150, 30, 500, 550)
            self.config_button(self.paga, str2, f, 150, 30, 750, 600)
            self.config_button(self.cancel, str3, f, 150, 30, 300, 550)
            self.config_button(self.aggiungi, str4, f, 150, 30, 100, 550)
        if not self.isNuovo:
            self.config_button(self.ok, str5, f, 150, 30, 387.5, 550)
            self.config_button(self.paga, str2, f, 150, 30, 562.5, 550)
            self.config_button(self.cancel, str3, f, 150, 30, 212.5, 550)
            self.config_button(self.aggiungi, str4, f, 150, 30, 37.5, 550)
        self.aggiungi.clicked.connect(self.agg)
        self.cancel.clicked.connect(self.cancella)
        self.ok.clicked.connect(self.conferma)
        self.paga.clicked.connect(self.chiudi_conto)

        self.genera_lista()

        for mp in self.lmatprimec.get_lista_mp():
            self.cb.addItem(mp.nome + " €" + str(mp.prezzo))
            self.cb.setFont(font)

        self.tab_widget.setFixedSize(700, 500)
        self.tab_widget.move(25, 25)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.widget, str6)
        self.tab_widget.addTab(self.tutto, str7)

        self.config_layout(self.cb, self.widget)
        self.config_layout2(self.lista, self.lista_totale, self.tutto)

    def agg(self):
        a = self.tab_widget.currentIndex()
        f, d = 1250, 500
        if a == 0:
            self.matprime_ordine.append((self.nome(self.cb.currentText()), self.prezzo(self.cb.currentText())))
            winsound.Beep(f, d)
        self.genera_lista()

    def genera_lista(self):

        global str17, str18, str19, str20
        if self.lingua == "Inglese":
            str17 = "Empty order!"
            str18 = "Product"
            str19 = "Price"
            str20 = "Total"
        if self.lingua == "Italiano":
            str17 = "Ordine vuoto!"
            str18 = "Prodotto"
            str19 = "Prezzo"
            str20 = "Totale"

        if not self.matprime_ordine:
            self.lista.setItem(0, 0, QTableWidgetItem(str17))
            self.lista.setItem(0, 1, QTableWidgetItem(""))
            self.lista_totale.setItem(0, 0, QTableWidgetItem(str17))
            self.lista_totale.setItem(0, 1, QTableWidgetItem("0"))
        else:
            self.lista.setColumnCount(2)
            self.lista.setColumnWidth(0, 200)
            self.lista_totale.setColumnCount(2)
            self.lista_totale.setRowCount(1)
            self.lista_totale.setColumnWidth(0, 200)
            self.lista_totale.setEnabled(False)
            self.lista_totale.setHorizontalHeaderLabels([str18, str19])
            self.conto_finale = 0
            a = 0
            self.lista.setHorizontalHeaderLabels([str18, str19])
            for row, data in enumerate(self.matprime_ordine):
                a += 1
                self.lista.setRowCount(a)
                nome, prezzo = data
                item = QTableWidgetItem(nome)
                item2 = QTableWidgetItem("€" + str(prezzo))
                self.lista.setItem(row, 0, item)
                self.lista.setItem(row, 1, item2)
                self.conto_finale += prezzo
            self.lista_totale.setItem(0, 0, QTableWidgetItem(str20))
            self.lista_totale.setItem(0, 1, QTableWidgetItem("€" + str(self.conto_finale)))

    def conferma(self):

        global str21, str22, str23, str24
        if self.lingua == "Inglese":
            str21 = "To confirm go to the final screen!"
            str22 = "Insert at least one product!"
            str23 = "Order placed correctly!"
            str24 = "Order changed successfully!"
        if self.lingua == "Italiano":
            str21 = "Per confermare andare alla schermata finale!"
            str22 = "Inserire almeno un prodotto!"
            str23 = "Ordine effettuato correttamente!"
            str24 = "Ordine modificato correttamente!"

        if self.tab_widget.currentIndex() != 1:
            QMessageBox.warning(None, "RGest", str21)
        else:
            if not self.matprime_ordine:
                QMessageBox.warning(None, "RGest", str22)
            else:
                if self.isNuovo:
                    self.controller.aggiungi_ordineMP(ordineMP_model(self.matprime_ordine))
                    QMessageBox.information(None, "RGest", str23)
                if not self.isNuovo:
                    self.contr.set_mp_list(self.matprime_ordine)
                    QMessageBox.information(None, "RGest", str24)
                self.callback()
                self.close()

    def cancella(self):

        global str25, str26, str27
        if self.lingua == "Inglese":
            str25 = "To delete a product go to the final screen!"
            str26 = "Select a product!"
            str27 = "Empty order!"
        if self.lingua == "Italiano":
            str25 = "Per eliminare un prodotto andare alla schermata finale!"
            str26 = "Selezionare un prodotto!"
            str27 = "Ordine vuoto!"

        if self.tab_widget.currentIndex() != 1:
            QMessageBox.warning(None, "RGest", str25)
        else:
            if not self.lista.selectedItems():
                QMessageBox.warning(None, "RGest", str26)
            else:
                if not self.matprime_ordine:
                    QMessageBox.warning(None, "RGest", str27)
                else:
                    selected = self.lista.selectedItems()[0].row()
                    self.matprime_ordine.pop(selected)
                    self.genera_lista()

    def chiudi_conto(self):

        global str28, str29
        if self.lingua == "Inglese":
            str28 = "Order paid! Costs and statistics on purchased raw materials stored correctly!"
            str29 = "Empty order!"
        if self.lingua == "Italiano":
            str28 = "Ordine pagato! Costi e statistiche sulle materie prime acquistate memorizzati correttamente!"
            str29 = "Ordine vuoto!"

        if not self.matprime_ordine:
            QMessageBox.warning(None, "RGest", str29)
        else:
            self.lcMPc.aggiungi_contoMP(contoMP_model(self.conto_finale))
            for mp in self.matprime_ordine:
                self.lmatprimec.aggiungi_inMag(mp)
            self.controller.elimina(self.ordine)
            self.callback()
            QMessageBox.information(None, "RGest", str28)
            self.close()

    def config_layout2(self, tw, tw2, widget):
        layout = QGridLayout(self)
        layout.addWidget(tw, 0, 0)
        layout.addWidget(tw2, 0, 1)
        widget.setLayout(layout)

    def config_layout(self, tw, widget):
        layout = QGridLayout(self)
        layout.addWidget(tw, 0, 0)
        widget.setLayout(layout)

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def prezzo(self, cb):
        b = self.trova(cb)
        c = cb[b:]
        return float(c)

    def nome(self, cb):
        b = self.trova(cb) - 2
        c = cb[:b]
        return c

    def trova(self, stringa):
        carattere = "€"
        indice = 0
        while indice < len(stringa):
            if stringa[indice] == carattere:
                return indice + 1
            indice = indice + 1
        return -1

    def closeEvent(self, event):
        self.lcMPc.save_data()
        self.lmatprimec.save_data_magazzino()
