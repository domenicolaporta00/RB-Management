from PyQt5.QtCore import QDate, QTime


class conto_model():

    def __init__(self, conto):
        self.data = QDate.currentDate().toString("dddd d MMMM yyyy")
        self.orario = QTime.currentTime().toString("hh:mm")
        self.conto = conto
