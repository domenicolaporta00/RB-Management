from Lista_prenotazioni.model.lista_prenotazioni_model import lista_prenotazioni_model


class lista_prenotazioni_controller:

    def __init__(self):
        super(lista_prenotazioni_controller, self).__init__()
        self.lpm = lista_prenotazioni_model()

    def aggiungi_prenotazione(self, prenotazione, orario):
        self.lpm.aggiungi_prenotazione(prenotazione, orario)

    def get_prenotazione(self, i):
        return self.lpm.get_prenotazione(i)

    def get_prenotazione_cena(self, i):
        return self.lpm.get_prenotazione_cena(i)

    def get_lista_prenotazioni(self):
        return self.lpm.get_lista_prenotazioni()

    def get_lista_prenotazioni_cena(self):
        return self.lpm.get_lista_prenotazioni_cena()

    def cancel(self):
        self.lpm.cancel()

    def cancel_cena(self):
        self.lpm.cancel_cena()

    def save_data(self):
        self.lpm.save_data()
