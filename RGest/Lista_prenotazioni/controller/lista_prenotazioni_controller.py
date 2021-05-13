from Lista_prenotazioni.model.lista_prenotazioni_model import lista_prenotazioni_model

class lista_prenotazioni_controller:

    def __init__(self):
        super(lista_prenotazioni_controller, self).__init__()
        self.lpm = lista_prenotazioni_model()

    def aggiungi_prenotazione(self, prenotazione):
        self.lpm.aggiungi_prenotazione(prenotazione)

    def get_prenotazione(self, i):
        return self.lpm.get_prenotazione(i)

    def get_lista_prenotazioni(self):
        return self.lpm.get_lista_prenotazioni()

    #def cancella(self, tavolo):
     #   self.lpm.cancel(tavolo)

    def cancel(self):
        self.lpm.cancel()

    def save_data(self):
        self.lpm.save_data()