class costi_covid_controller():

    def __init__(self, costi_covid):
        self.cv = costi_covid

    def get_mascherine(self):
        return self.cv.mascherine

    def get_gel(self):
        return self.cv.gel

    def get_guanti(self):
        return self.cv.guanti

    def get_igienizzante(self):
        return self.cv.igienizzante

    def get_disinfestazione(self):
        return self.cv.disinfestazione

    def get_data(self):
        return self.cv.data

    def get_totale(self):
        return self.cv.totale

    def set_mascherine(self, mascherine):
        self.cv.mascherine = mascherine

    def set_gel(self, gel):
        self.cv.gel = gel

    def set_guanti(self, guanti):
        self.cv.guanti = guanti

    def set_igienizzante(self, igienizzante):
        self.cv.igienizzante = igienizzante

    def set_disinfestazione(self, disinfestazione):
        self.cv.disinfestazione = disinfestazione