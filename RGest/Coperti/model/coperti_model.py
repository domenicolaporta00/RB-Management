from PyQt5.QtCore import QDate


class coperti_model():

    def __init__(self, n):
        self.n = n
        self.data = QDate.currentDate().toString("ddd d MMM yyyy")
        #self.orario = QTime.currentTime().toString("hh:mm")
        self.ricavo_tot = 2*n
        #self.conto = conto
