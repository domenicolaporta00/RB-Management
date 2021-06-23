from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QMainWindow, QListView, QPushButton, QLabel, QMessageBox

from Lista_comande.controller.lista_comande_controller import lista_comande_controller
from Lista_comande.view.inserisci_comanda_view import inserisci_comanda_view


class lista_comande_view(QMainWindow):

    def __init__(self):
        super(lista_comande_view, self).__init__()

        self.lcomandec = lista_comande_controller()

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
        font = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lista.move(125, 100)
        self.lista.setFixedSize(500, 400)

        self.lista_label.setText("Elenco delle comande")
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(225, 40)
        self.lista_label.setFixedSize(300, 40)

        self.config_button(self.aggiungi, "Aggiungi", font, 150, 30, 200, 550)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.visualizza, "Visualizza", font, 150, 30, 400, 550)
        self.visualizza.clicked.connect(self.mostra)

    def genera_lista(self):
        self.list_view_model = QStandardItemModel(self.lista)
        n = 1
        for comanda in self.lcomandec.get_lista_comande():
            item = QStandardItem()
            item.setText(
                "Ordine numero " + str(n) + ", " + str(comanda.numero) + " piatti")
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
            n += 1
        self.lista.setModel(self.list_view_model)

    def apri_inserimento(self):
        self.newelement()

    def newelement(self):
        self.closeEvent(self.lcomandec.save_data())
        self.icv = inserisci_comanda_view(self.lcomandec, self.genera_lista, [], True)
        self.icv.show()

    def mostra(self):
        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare un ordine!")
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

    def closeEvent(self, event):
        self.lcomandec.save_data()
