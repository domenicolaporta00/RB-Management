from PyQt5.QtCore import QDate


class cliente_model():
    def __init__(self, nome, telefono):
        self.nome = nome
        self.telefono = telefono
        self.data = QDate.currentDate().toString("dddd d MMMM yyyy")