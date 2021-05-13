import os
import pickle

class lista_prenotazioni_model():

    def __init__(self):
        super(lista_prenotazioni_model, self).__init__()
        self.lista_prenotazioni = []
        if os.path.isfile("Lista_prenotazioni\\data\\lista_prenotazioni_salvata.pickle"):
            with open("Lista_prenotazioni\\data\\lista_prenotazioni_salvata.pickle", "rb") as f:
                self.lista_prenotazioni = pickle.load(f)

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    #def cancel(self, tavolo):
     #   def flag(prenotazione):
      #      if prenotazione.tavolo == tavolo:
       #         return True
        #    return False
        #self.lista_prenotazioni.remove(list(filter(flag, self.lista_prenotazioni))[0])

    def get_prenotazione(self, i):
        return self.lista_prenotazioni[i]

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def cancel(self):
        self.lista_prenotazioni = []

    def save_data(self):
        with open("Lista_prenotazioni\\data\\lista_prenotazioni_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)