import os
import pickle


class lista_tasse_model():

    def __init__(self):
        super(lista_tasse_model, self).__init__()
        self.lista_tasse = []
        if os.path.isfile("Lista_tasse\\data\\lista_tasse_salvata.pickle"):
            with open("Lista_tasse\\data\\lista_tasse_salvata.pickle", "rb") as f:
                self.lista_tasse = pickle.load(f)

    def aggiungi_tasse(self, tax):
        self.lista_tasse.append(tax)

    def get_tax(self, i):
        return self.lista_tasse[i]

    def get_lista_tasse(self):
        return self.lista_tasse

    def cancel(self):
        self.lista_tasse = []

    def save_data(self):
        with open("Lista_tasse\\data\\lista_tasse_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_tasse, handle, pickle.HIGHEST_PROTOCOL)
