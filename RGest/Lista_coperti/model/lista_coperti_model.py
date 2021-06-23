import os
import pickle


class lista_coperti_model():

    def __init__(self):
        super(lista_coperti_model, self).__init__()
        self.lista_coperti = []
        self.lista_conto = []
        if os.path.isfile("Lista_coperti\\data\\lista_coperti_salvata.pickle"):
            with open("Lista_coperti\\data\\lista_coperti_salvata.pickle", "rb") as f:
                self.lista_coperti = pickle.load(f)
        if os.path.isfile("Lista_coperti\\data\\lista_conto_salvata.pickle"):
            with open("Lista_coperti\\data\\lista_conto_salvata.pickle", "rb") as F:
                self.lista_conto = pickle.load(F)

    def aggiungi_coperto(self, c):
        self.lista_coperti.append(c)

    def aggiungi_conto(self, conto):
        self.lista_conto.append(conto)

    def get_coperto(self, i):
        return self.lista_coperti[i]

    def get_conto(self, index):
        return self.lista_conto[index]

    def get_lista_coperti(self):
        return self.lista_coperti

    def get_lista_conto(self):
        return self.lista_conto

    def cancel(self):
        self.lista_coperti = []

    def cancel_conto(self):
        self.lista_conto = []

    def save_data(self):
        with open("Lista_coperti\\data\\lista_coperti_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_coperti, handle, pickle.HIGHEST_PROTOCOL)

    def save_data_conto(self):
        with open("Lista_coperti\\data\\lista_conto_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_conto, handle, pickle.HIGHEST_PROTOCOL)
