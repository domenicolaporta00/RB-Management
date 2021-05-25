import os
import pickle

class lista_dipendenti_model():

    def __init__(self):
        super(lista_dipendenti_model, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile("Lista_dipendenti\\data\\lista_dipendenti_salvata.pickle"):
            with open("Lista_dipendenti\\data\\lista_dipendenti_salvata.pickle", "rb") as f:
                self.lista_dipendenti = pickle.load(f)

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def get_dipendente(self, i):
        return self.lista_dipendenti[i]

    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    def remove_dipendente(self, id):
        def flag(dipendente):
            if dipendente.id == id:
                return True
            return False
        self.lista_dipendenti.remove(list(filter(flag, self.lista_dipendenti))[0])

    def cancel(self):
        self.lista_dipendenti = []

    def save_data(self):
        with open("Lista_dipendenti\\data\\lista_dipendenti_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)