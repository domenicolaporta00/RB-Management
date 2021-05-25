from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QMainWindow, QListView, QPushButton, QMessageBox, QLabel

from Dipendente.view.dipendente_view import dipendente_view
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller
from Lista_dipendenti.view.inserisci_dipendente_view import inserisci_dipendente_view


class lista_dipendenti_view(QMainWindow):

    def __init__(self):
        super(lista_dipendenti_view, self).__init__()

        self.ldc = lista_dipendenti_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QListView(self)

        self.aggiungi = QPushButton(self)
        self.visualizza = QPushButton(self)
        self.elimina = QPushButton(self)

        self.lista_label = QLabel(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11, QFont.Bold)

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lista.move(125, 100)
        self.lista.setFixedSize(500, 400)

        self.lista_label.setText("Elenco dei dipendenti")
        self.lista_label.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.lista_label.setStyleSheet("color: red")
        self.lista_label.move(200, 40)
        self.lista_label.setFixedSize(350, 40)

        self.config_button(self.aggiungi, "Aggiungi", font, 150, 30, 100, 550)
        self.aggiungi.clicked.connect(self.apri_inserimento)
        self.config_button(self.visualizza, "Modifica", font, 150, 30, 500, 550)
        self.visualizza.clicked.connect(self.mostra_dipendente)
        self.config_button(self.elimina, "Elimina tutto", font, 150, 30, 300, 550)
        self.elimina.clicked.connect(self.cancel)

    def genera_lista(self):
        self.list_view_model = QStandardItemModel(self.lista)
        for dipendente in self.ldc.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.postazione+", "+dipendente.ruolo +", "+dipendente.cognome+" "+dipendente.nome)
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
        self.lista.setModel(self.list_view_model)

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def apri_inserimento(self):
        self.newelement()

    def mostra_dipendente(self):
        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", "Selezionare un dipendente!")
        else:
            selected = self.lista.selectedIndexes()[0].row()
            dipendente_selezionato = self.ldc.get_dipendente(selected)
            self.dv = dipendente_view(dipendente_selezionato, self.ldc.remove_dipendente, self.genera_lista)
            self.dv.show()

    def cancel(self):
        self.ldc.cancel()
        self.ldc.save_data()
        self.genera_lista()
        QMessageBox.information(None, "RGest", "Tutte i dipendenti sono stati cancellati!")

    def newelement(self):
        self.closeEvent(self.ldc.save_data())
        self.idv = inserisci_dipendente_view(self.ldc, self.genera_lista)
        self.idv.show()

    def closeEvent(self, event):
        self.ldc.save_data()