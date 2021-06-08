import os
import pickle

from PyQt5.QtCore import QTime


class lista_prenotazioni_model():

    def __init__(self):
        super(lista_prenotazioni_model, self).__init__()
        self.lista_prenotazioni = []
        self.lista_prenotazioni_cena = []
        if os.path.isfile("Lista_prenotazioni\\data\\lista_prenotazioni_salvata.pickle"):
            with open("Lista_prenotazioni\\data\\lista_prenotazioni_salvata.pickle", "rb") as f:
                self.lista_prenotazioni = pickle.load(f)
                print(self.lista_prenotazioni)
        if os.path.isfile("Lista_prenotazioni\\data\\lista_prenotazioni_cena_salvata.pickle"):
            with open("Lista_prenotazioni\\data\\lista_prenotazioni_cena_salvata.pickle", "rb") as f:
                self.lista_prenotazioni_cena = pickle.load(f)
                print(self.lista_prenotazioni_cena)

    def aggiungi_prenotazione(self, prenotazione, orario):
        if QTime(14, 00) >= orario >= QTime(12, 00):
            self.lista_prenotazioni.append(prenotazione)
        if QTime(22, 00) >= orario >= QTime(19, 00):
            self.lista_prenotazioni_cena.append(prenotazione)

    # def cancel(self, tavolo):
    #   def flag(prenotazione):
    #      if prenotazione.tavolo == tavolo:
    #         return True
    #    return False
    # self.lista_prenotazioni.remove(list(filter(flag, self.lista_prenotazioni))[0])

    def get_prenotazione(self, i):
        return self.lista_prenotazioni[i]

    def get_prenotazione_cena(self, i):
        return self.lista_prenotazioni_cena[i]

    def get_lista_prenotazioni(self):
        return self.lista_prenotazioni

    def get_lista_prenotazioni_cena(self):
        return self.lista_prenotazioni_cena

    def cancel(self):
        self.lista_prenotazioni = []

    def cancel_cena(self):
        self.lista_prenotazioni_cena = []

    def save_data(self):
        with open("Lista_prenotazioni\\data\\lista_prenotazioni_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioni, handle, pickle.HIGHEST_PROTOCOL)
        with open("Lista_prenotazioni\\data\\lista_prenotazioni_cena_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_prenotazioni_cena, handle, pickle.HIGHEST_PROTOCOL)
