from PyQt5.QtCore import QDate


class tasse_model():

    def __init__(self, acqua, luce, gas, tv, affitto):
        self.acqua = acqua
        self.luce = luce
        self.gas = gas
        self.tv = tv
        self.affitto = affitto
        self.data = QDate.currentDate().toString("dddd d MMMM yyyy")
