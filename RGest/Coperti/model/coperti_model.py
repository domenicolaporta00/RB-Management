from PyQt5.QtCore import QDate


class coperti_model():

    def __init__(self, n):
        self.n = n
        self.data = QDate.currentDate().toString("dddd d MMMM yyyy")
        self.ricavo_tot = 2*n
