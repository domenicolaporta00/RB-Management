import os
import pickle


class lista_comande_model():

    def __init__(self):
        super(lista_comande_model, self).__init__()
        self.lista_comande = []
        if os.path.isfile("Lista_comande\\data\\lista_comande_salvata.pickle"):
            with open("Lista_comande\\data\\lista_comande_salvata.pickle", "rb") as f:
                self.lista_comande = pickle.load(f)

    def aggiungi_comanda(self, comanda):
        self.lista_comande.append(comanda)

    def get_comanda(self, i):
        return self.lista_comande[i]

    def get_lista_comande(self):
        return self.lista_comande

    def cancel(self):
        self.lista_comande = []

    def elimina(self, i):
        self.lista_comande.remove(i)

    def save_data(self):
        with open("Lista_comande\\data\\lista_comande_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_comande, handle, pickle.HIGHEST_PROTOCOL)
