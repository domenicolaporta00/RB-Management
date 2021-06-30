from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QPushButton, QTabWidget, QWidget, QComboBox, QLabel, \
    QTableWidgetItem, QMessageBox, QGridLayout

from ContoMP.model.contoMP_model import contoMP_model
from Lista_contiMP.controller.lista_contiMP_controller import lista_contiMP_controller
from Lista_materie_prime.controller.lista_materie_prime_controller import lista_materie_prime_controller
from Lista_ordiniMP.controller.lista_ordiniMP_controller import lista_ordiniMP_controller
from Lista_piatti.controller.lista_piatti_controller import lista_piatti_controller
from OrdineMP.controller.ordineMP_controller import ordineMP_controller
from OrdineMP.model.ordineMP_model import ordineMP_model


class inserisci_ordineMP_view(QMainWindow):

    def __init__(self, controller, callback, elenco, isNuovo, ordine=None):
        super(inserisci_ordineMP_view, self).__init__()

        self.matprime_ordine = elenco
        self.controller = controller
        self.callback = callback
        self.jsonobject = {}
        self.isNuovo = isNuovo
        self.ordine = ordine
        self.contr = ordineMP_controller(ordine)
        # self.isDelivery = isDelivery

        # self.lcomandac = lista_ordiniMP_controller()  #  non serve, già passato nel costruttore
        self.lmatprimec = lista_materie_prime_controller()  # per prendere le mp originali e per memorizzare le stats
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
        # self.lpiattic.cancel_stats()
        font = QFont("Times Roman", 11)
        f = QFont("Times Roman", 11, QFont.Bold)

        if self.isNuovo:
            self.config_button(self.ok, "Conferma", f, 150, 30, 500, 550)
            self.config_button(self.paga, "Chiudi ordine", f, 150, 30, 750, 600)
            self.config_button(self.cancel, "Elimina", f, 150, 30, 300, 550)
            self.config_button(self.aggiungi, "Aggiungi", f, 150, 30, 100, 550)
        if not self.isNuovo:
            self.config_button(self.ok, "Modifica", f, 150, 30, 387.5, 550)
            self.config_button(self.paga, "Chiudi ordine", f, 150, 30, 562.5, 550)
            self.config_button(self.cancel, "Elimina", f, 150, 30, 212.5, 550)
            self.config_button(self.aggiungi, "Aggiungi", f, 150, 30, 37.5, 550)
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
        self.tab_widget.addTab(self.widget, "Ordine")
        self.tab_widget.addTab(self.tutto, "Totale")

        self.config_layout(self.cb, self.widget)
        self.config_layout2(self.lista, self.lista_totale, self.tutto)

    def agg(self):
        a = self.tab_widget.currentIndex()
        if a == 0:
            self.matprime_ordine.append((self.nome(self.cb.currentText()), self.prezzo(self.cb.currentText())))
        self.genera_lista()

    def genera_lista(self):
        if not self.matprime_ordine:
            self.lista.setItem(0, 0, QTableWidgetItem("Ordine vuoto!"))
            self.lista.setItem(0, 1, QTableWidgetItem(""))
            self.lista_totale.setItem(0, 0, QTableWidgetItem("Ordine vuoto!"))
            self.lista_totale.setItem(0, 1, QTableWidgetItem("0"))
        else:
            self.lista.setColumnCount(2)
            self.lista.setColumnWidth(0, 200)
            self.lista_totale.setColumnCount(2)
            self.lista_totale.setRowCount(1)
            self.lista_totale.setColumnWidth(0, 200)
            self.lista_totale.setEnabled(False)
            self.lista_totale.setHorizontalHeaderLabels(["Prodotto", "Prezzo"])
            self.conto_finale = 0
            a = 0
            self.lista.setHorizontalHeaderLabels(["Prodotto", "Prezzo"])
            for row, data in enumerate(self.matprime_ordine):
                a += 1
                self.lista.setRowCount(a)
                nome, prezzo = data
                item = QTableWidgetItem(nome)
                item2 = QTableWidgetItem("€" + str(prezzo))
                self.lista.setItem(row, 0, item)
                self.lista.setItem(row, 1, item2)
                self.conto_finale += prezzo
            self.lista_totale.setItem(0, 0, QTableWidgetItem("Totale"))
            self.lista_totale.setItem(0, 1, QTableWidgetItem("€" + str(self.conto_finale)))

    def conferma(self):
        if self.tab_widget.currentIndex() != 1:
            QMessageBox.warning(None, "RGest", "Per confermare andare alla schermata finale!")
        else:
            if not self.matprime_ordine:
                QMessageBox.warning(None, "RGest", "Inserire almeno un prodotto!")
            else:
                if self.isNuovo:
                    self.controller.aggiungi_ordineMP(ordineMP_model(self.matprime_ordine))
                    QMessageBox.information(None, "RGest", "Ordine effettuato correttamente!")
                if not self.isNuovo:
                    self.contr.set_mp_list(self.matprime_ordine)
                    QMessageBox.information(None, "RGest", "Ordine modificato correttamente!")
                self.callback()
                self.close()

    def cancella(self):
        if self.tab_widget.currentIndex() != 1:
            QMessageBox.warning(None, "RGest", "Per eliminare un prodotto andare alla schermata finale!")
        else:
            if not self.lista.selectedItems():
                QMessageBox.warning(None, "RGest", "Selezionare un prodotto!")
            else:
                if not self.matprime_ordine:
                    QMessageBox.warning(None, "RGest", "Ordine vuoto!")
                else:
                    selected = self.lista.selectedItems()[0].row()
                    self.matprime_ordine.pop(selected)
                    self.genera_lista()

    def chiudi_conto(self):
        if not self.matprime_ordine:
            QMessageBox.warning(None, "RGest", "Ordine vuoto!")
        else:
            self.lcMPc.aggiungi_contoMP(contoMP_model(self.conto_finale))
            for mp in self.matprime_ordine:
                print(mp)
                # self.lpiattic.aggiungi_stat(mp) prima creare le stats
            self.controller.elimina(self.ordine)
            self.callback()
            QMessageBox.information(None, "RGest", "Ordine pagato! Costi e statistiche sulle materie prime acquistate "
                                                   "memorizzati correttamente!")
            self.close()
            # print("len stats =", len(self.lpiattic.get_lista_stats()))

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
        # self.lpiattic.save_data_stats() prima fare le stats
