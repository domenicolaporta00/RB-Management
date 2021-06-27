from PyQt5.QtCore import QDate


class consegna_delivery_model():

    def __init__(self, n):
        self.n = n
        self.data = QDate.currentDate().toString("dddd d MMMM yyyy")
        # self.orario = QTime.currentTime().toString("hh:mm")
        self.ricavo_tot = 5*n
        # self.conto = conto
