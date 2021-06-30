import os
import pickle


class lista_ordiniMP_model():

    def __init__(self):
        super(lista_ordiniMP_model, self).__init__()
        self.lista_ordiniMP = []
        if os.path.isfile("Lista_ordiniMP\\data\\lista_ordiniMP_salvata.pickle"):
            with open("Lista_ordiniMP\\data\\lista_ordiniMP_salvata.pickle", "rb") as f:
                self.lista_ordiniMP = pickle.load(f)

    def aggiungi_ordineMP(self, ordineMP):
        self.lista_ordiniMP.append(ordineMP)

    def get_ordineMP(self, i):
        return self.lista_ordiniMP[i]

    def get_lista_ordiniMP(self):
        return self.lista_ordiniMP

    def cancel(self):
        self.lista_ordiniMP = []

    def elimina(self, i):
        self.lista_ordiniMP.remove(i)

    def save_data(self):
        with open("Lista_ordiniMP\\data\\lista_ordiniMP_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_ordiniMP, handle, pickle.HIGHEST_PROTOCOL)
