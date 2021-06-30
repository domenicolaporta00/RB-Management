from PyQt5.QtCore import QDate

class costi_covid_model():

    def __init__(self, mascherine, gel, guanti, igienizzanti, disinfestazione):
        self.mascherine = mascherine
        self.gel = gel
        self.guanti = guanti
        self.igienizzanti = igienizzanti
        self.disinfestazione = disinfestazione
        self.data = QDate.currentDate().toString("ddd d MMM yyyy")
        self.totale = float(mascherine) + float(gel) + float(guanti) + float(igienizzanti) + float(disinfestazione)
