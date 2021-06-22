from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTabWidget, QWidget, QComboBox, QGridLayout, QMessageBox, QLabel, \
    QTableWidget, QTableWidgetItem

from Comanda.controller.comanda_controller import comanda_controller
from Comanda.model.comanda_model import comanda_model
from Lista_comande.controller.lista_comande_controller import lista_comande_controller
from Lista_piatti.controller.lista_piatti_controller import lista_piatti_controller


class inserisci_comanda_view(QMainWindow):

    def __init__(self, controller, callback, elenco, isNuovo, ordine=None):
        super(inserisci_comanda_view, self).__init__()

        self.piatti_ordine = elenco
        self.controller = controller
        self.callback = callback
        self.jsonobject = {}
        self.isNuovo = isNuovo
        self.contr = comanda_controller(ordine)

        self.lcomandac = lista_comande_controller()
        self.lpiattic = lista_piatti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        # self.lista = QListView(self)
        self.lista = QTableWidget(self)

        self.ok = QPushButton(self)
        self.aggiungi = QPushButton(self)
        self.cancel = QPushButton(self)

        self.tab_widget = QTabWidget(self)
        self.antipasti = QWidget(self)
        self.primi = QWidget(self)
        self.secondi = QWidget(self)
        self.contorni = QWidget(self)
        self.dolci = QWidget(self)
        self.frutta = QWidget(self)
        self.digestivi = QWidget(self)
        self.intolleranze = QWidget(self)
        self.bevande = QWidget(self)
        self.tutto = QWidget(self)

        self.cba = QComboBox(self)
        self.cbp = QComboBox(self)
        self.cbs = QComboBox(self)
        self.cbc = QComboBox(self)
        self.cbdo = QComboBox(self)
        self.cbf = QComboBox(self)
        self.cbdi = QComboBox(self)
        self.cbb = QComboBox(self)

        self.piatto1 = QLabel(self)
        self.piatto2 = QLabel(self)
        self.piatto3 = QLabel(self)
        self.piatto4 = QLabel(self)
        self.piatto5 = QLabel(self)
        self.piatto6 = QLabel(self)
        self.piatto7 = QLabel(self)
        self.piatto8 = QLabel(self)
        self.piatto9 = QLabel(self)
        self.piatto10 = QLabel(self)
        self.piatto11 = QLabel(self)
        self.piatto12 = QLabel(self)
        self.piatto13 = QLabel(self)
        self.piatto14 = QLabel(self)
        self.piatto15 = QLabel(self)
        self.piatto16 = QLabel(self)
        self.piatto17 = QLabel(self)
        self.piatto18 = QLabel(self)
        self.piatto19 = QLabel(self)
        self.piatto20 = QLabel(self)
        self.piatto21 = QLabel(self)
        self.piatto22 = QLabel(self)

        self.listaAntipasti = [self.piatto1, self.piatto2]
        self.listaPrimi = [self.piatto3, self.piatto4, self.piatto5, self.piatto6]
        self.listaSecondi = [self.piatto7, self.piatto8, self.piatto9]
        self.listaContorni = [self.piatto10, self.piatto11, self.piatto12]
        self.listaDolci = [self.piatto13, self.piatto14]
        self.listaFrutta = [self.piatto15]
        self.listaDigestivi = [self.piatto16, self.piatto17]
        self.listaBevande = [self.piatto18, self.piatto19, self.piatto20, self.piatto21, self.piatto22]
        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11)

        if self.isNuovo:
            self.config_button(self.ok, "Conferma", QFont("Times Roman", 11, QFont.Bold), 150, 30, 100, 550)
        if not self.isNuovo:
            self.config_button(self.ok, "Modifica", QFont("Times Roman", 11, QFont.Bold), 150, 30, 100, 550)
        self.config_button(self.aggiungi, "Aggiungi", QFont("Times Roman", 11, QFont.Bold), 150, 30, 300, 550)
        self.config_button(self.cancel, "Elimina", QFont("Times Roman", 11, QFont.Bold), 150, 30, 500, 550)
        self.aggiungi.clicked.connect(self.agg)
        self.cancel.clicked.connect(self.cancella)
        self.ok.clicked.connect(self.conferma)

        self.genera_lista()

        for piatti in self.lpiattic.get_lista_piatti():
            t = piatti.tipo
            if t == "antipasto":
                self.cba.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cba.setFont(font)
            elif t == "primo":
                self.cbp.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbp.setFont(font)
            elif t == "secondo":
                self.cbs.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbs.setFont(font)
            elif t == "contorno":
                self.cbc.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbc.setFont(font)
            elif t == "dolce":
                self.cbdo.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbdo.setFont(font)
            elif t == "frutta":
                self.cbf.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbf.setFont(font)
            elif t == "digestivo":
                self.cbdi.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbdi.setFont(font)
            elif t == "bevanda":
                self.cbb.addItem(piatti.nome + " €" + str(piatti.prezzo))
                self.cbb.setFont(font)

        self.tab_widget.setFixedSize(700, 500)
        self.tab_widget.move(25, 25)
        self.tab_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.tab_widget.setFont(font)
        self.tab_widget.addTab(self.intolleranze, "Intolleranze")
        self.tab_widget.addTab(self.antipasti, "Antipasti")
        self.tab_widget.addTab(self.primi, "Primi")
        self.tab_widget.addTab(self.secondi, "Secondi")
        self.tab_widget.addTab(self.contorni, "Contorni")
        self.tab_widget.addTab(self.dolci, "Dolci")
        self.tab_widget.addTab(self.frutta, "Frutta")
        self.tab_widget.addTab(self.digestivi, "Digestivi")
        self.tab_widget.addTab(self.bevande, "Bevande")
        self.tab_widget.addTab(self.tutto, "Totale")

        a = 1
        string = "images\\cutmypic"
        estensione = ".png"
        for ap in self.listaAntipasti:
            self.config_foto(ap, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for p in self.listaPrimi:
            self.config_foto(p, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for s in self.listaSecondi:
            self.config_foto(s, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for c in self.listaContorni:
            self.config_foto(c, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for do in self.listaDolci:
            self.config_foto(do, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for f in self.listaFrutta:
            self.config_foto(f, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for di in self.listaDigestivi:
            self.config_foto(di, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1
        for b in self.listaBevande:
            self.config_foto(b, QPixmap(string + str(a) + estensione), 250, 250)
            a += 1

        self.config_layout(self.cba, self.listaAntipasti, 0, 0, self.antipasti)
        self.config_layout(self.cbp, self.listaPrimi, 0, 0, self.primi)
        self.config_layout(self.cbs, self.listaSecondi, 0, 0, self.secondi)
        self.config_layout(self.cbc, self.listaContorni, 0, 0, self.contorni)
        self.config_layout(self.cbdo, self.listaDolci, 0, 0, self.dolci)
        self.config_layout(self.cbf, self.listaFrutta, 0, 0, self.frutta)
        self.config_layout(self.cbdi, self.listaDigestivi, 0, 0, self.digestivi)
        self.config_layout(self.cbb, self.listaBevande, 0, 0, self.bevande)
        self.config_layout2(self.lista, self.tutto)

    def agg(self):
        a = self.tab_widget.currentIndex()
        if a == 1:
            self.piatti_ordine.append((self.nome(self.cba.currentText()), self.prezzo(self.cba.currentText())))
        elif a == 2:
            self.piatti_ordine.append((self.nome(self.cbp.currentText()), self.prezzo(self.cbp.currentText())))
        elif a == 3:
            self.piatti_ordine.append((self.nome(self.cbs.currentText()), self.prezzo(self.cbs.currentText())))
        elif a == 4:
            self.piatti_ordine.append((self.nome(self.cbc.currentText()), self.prezzo(self.cbc.currentText())))
        elif a == 5:
            self.piatti_ordine.append((self.nome(self.cbdo.currentText()), self.prezzo(self.cbdo.currentText())))
        elif a == 6:
            self.piatti_ordine.append((self.nome(self.cbf.currentText()), self.prezzo(self.cbf.currentText())))
        elif a == 7:
            self.piatti_ordine.append((self.nome(self.cbdi.currentText()), self.prezzo(self.cbdi.currentText())))
        elif a == 8:
            self.piatti_ordine.append((self.nome(self.cbb.currentText()), self.prezzo(self.cbb.currentText())))
        self.genera_lista()

    def genera_lista(self):
        if not self.piatti_ordine:
            self.lista.setItem(0, 0, QTableWidgetItem("Ordine vuoto!"))
            self.lista.setItem(0, 1, QTableWidgetItem(""))
        else:
            self.lista.setColumnCount(2)
            self.lista.setColumnWidth(0, 200)
            a = 0
            self.lista.setHorizontalHeaderLabels(["Piatto", "Prezzo"])
            for row, data in enumerate(self.piatti_ordine):
                a += 1
                self.lista.setRowCount(a)
                nome, prezzo = data
                item = QTableWidgetItem(nome)
                item2 = QTableWidgetItem(str(prezzo))
                self.lista.setItem(row, 0, item)
                self.lista.setItem(row, 1, item2)

    def conferma(self):
        if self.tab_widget.currentIndex() != 9:
            QMessageBox.warning(None, "RGest", "Per confermare andare alla schermata finale!")
        else:
            if not self.piatti_ordine:
                QMessageBox.warning(None, "RGest", "Inserire almeno una portata!")
            else:
                if self.isNuovo:
                    self.controller.aggiungi_comanda(comanda_model(self.piatti_ordine))
                    QMessageBox.information(None, "RGest", "Ordine effettuato correttamente!")
                if not self.isNuovo:
                    self.contr.set_piatti_list(self.piatti_ordine)
                    QMessageBox.information(None, "RGest", "Ordine modificato correttamente!")
                self.callback()
                self.close()

    def cancella(self):
        if self.tab_widget.currentIndex() != 9:
            QMessageBox.warning(None, "RGest", "Per eliminare una portata andare alla schermata finale!")
        else:
            if not self.lista.selectedItems():
                QMessageBox.warning(None, "RGest", "Selezionare una portata!")
            else:
                if not self.piatti_ordine:
                    QMessageBox.warning(None, "RGest", "Ordine vuoto!")
                else:
                    selected = self.lista.selectedItems()[0].row()
                    self.piatti_ordine.pop(selected)
                    self.genera_lista()

    def config_layout2(self, tw, widget):
        layout = QGridLayout(self)
        layout.addWidget(tw, 0, 0)
        widget.setLayout(layout)

    def config_layout(self, cb, lista, c, d, widget):
        layout = QGridLayout(self)
        if not lista:
            pass
        if len(lista) == 1:
            layout.addWidget(lista[0], 0, 0)
            layout.addWidget(cb, 1, 0)
        if len(lista) == 2:
            for elem in lista:
                layout.addWidget(elem, c, d)
                d += 2
            layout.addWidget(cb, 1, 1)
        if len(lista) == 3:
            for elem in lista:
                if d == 2:
                    c += 1
                    d = 0
                layout.addWidget(elem, c, d)
                d += 1
            layout.addWidget(cb, 1, 1)
        if len(lista) == 4:
            for elem in lista:
                if d == 4:
                    c += 2
                    d = 0
                layout.addWidget(elem, c, d)
                d += 2
            layout.addWidget(cb, 1, 1)
        if len(lista) > 4:
            for elem in lista:
                if d == 3:
                    c += 1
                    d = 0
                if c == 1 and d == 1:
                    d = 2
                layout.addWidget(elem, c, d)
                d += 1
            layout.addWidget(cb, 1, 1)
        widget.setLayout(layout)

    def config_foto(self, layout, pixmap, a, b):
        layout.setPixmap(pixmap)
        layout.setFixedSize(a, b)

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
