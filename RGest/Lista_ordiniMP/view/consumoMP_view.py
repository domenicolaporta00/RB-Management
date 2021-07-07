from PyQt5.QtGui import QIcon, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QListView, QPushButton, QLabel, QMessageBox

from Lista_materie_prime.controller.lista_materie_prime_controller import lista_materie_prime_controller


class consumoMP_view(QMainWindow):

    def __init__(self, lingua):
        super(consumoMP_view, self).__init__()

        self.lingua = lingua

        self.lmatprimec = lista_materie_prime_controller()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.lista = QListView(self)

        self.elimina = QPushButton(self)

        self.lista_label = QLabel(self)

        self.schermata()

    def schermata(self):

        global str1, str2
        if self.lingua == "Inglese":
            str1 = "Select a product to delete"
            str2 = "Delete"
        if self.lingua == "Italiano":
            str1 = "Seleziona un prodotto da eliminare"
            str2 = "Elimina"

        font = QFont("Times Roman", 11, QFont.Bold)
        f = QFont("Times Roman", 20, QFont.Bold)

        self.genera_lista()
        self.lista.setModel(self.list_view_model)
        self.lista.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lista.move(125, 100)
        self.lista.setFixedSize(500, 400)
        self.lista.setSelectionMode(2)

        self.config_label(self.lista_label, str1, 135, 40, 480, 40, f)

        self.config_button(self.elimina, str2, font, 150, 30, 300, 550)
        self.elimina.clicked.connect(self.elimina_click)

    def genera_lista(self):
        self.list_view_model = QStandardItemModel(self.lista)
        n = 1
        for matPrima in self.lmatprimec.get_lista_magazzino():
            item = QStandardItem()
            item.setText(matPrima[0])
            item.setEditable(False)
            item.setFont(QFont("Times Roman", 11, QFont.Bold))
            self.list_view_model.appendRow(item)
            n += 1
        self.lista.setModel(self.list_view_model)

    def elimina_click(self):

        global str11, str21
        if self.lingua == "Inglese":
            str11 = "Select a product!"
            str21 = "Products deleted successfully!"
        if self.lingua == "Italiano":
            str11 = "Selezionare un prodotto!"
            str21 = "Prodotti eliminati correttamente!"

        if not self.lista.selectedIndexes():
            QMessageBox.warning(None, "RGest", str11)
        else:
            lista_ordinata = []
            selected_list = self.lista.selectedIndexes()
            selected_list.sort(reverse=True)
            for i in range(len(selected_list)):
                MP_selected_index = selected_list[i].row()
                lista_ordinata.append(MP_selected_index)
            for i in range(len(lista_ordinata)):
                MP_selected = self.lmatprimec.get_mp_inMag(lista_ordinata[i])
                self.lmatprimec.elimina_MP_daMag(MP_selected)
            QMessageBox.warning(None, "RGest", str21)
            self.genera_lista()

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

    def config_label(self, label, text, x, y, a, b, font):
        label.setText(text)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("color: red")
        label.setFixedSize(a, b)

    def closeEvent(self, event):
        self.lmatprimec.save_data_magazzino()
