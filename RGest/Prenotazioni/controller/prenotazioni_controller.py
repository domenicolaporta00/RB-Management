from Prenotazioni.model.prenotazioni_model import prenotazioni_model


class prenotazioni_controller():

    def __init__(self, prenotazione):
        self.pm = prenotazione

    def set_cognome(self, cognome):
        self.pm.cognome = cognome

    def set_posti(self, posti):
        self.pm.posti = posti

    def set_orario(self, orario):
        self.pm.orario = orario

    def set_info(self, info):
        self.pm.info = info

    def set_telefono(self, telefono):
        self.pm.telefono = telefono

    def set_tavolo(self, tavolo):
        self.pm.tavolo = tavolo

    def get_cognome(self):
        return self.pm.cognome

    def get_posti(self):
        return self.pm.posti

    def get_orario(self):
        return self.pm.orario

    def get_info(self):
        return self.pm.info

    def get_telefono(self):
        return self.pm.telefono

    def get_tavolo(self):
        return self.pm.tavolo