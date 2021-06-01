import os
import pickle


class lista_coperti_model():

    def __init__(self):
        super(lista_coperti_model, self).__init__()
        self.lista_coperti = []
        if os.path.isfile("Lista_coperti\\data\\lista_coperti_salvata.pickle"):
            with open("Lista_coperti\\data\\lista_coperti_salvata.pickle", "rb") as f:
                self.lista_coperti = pickle.load(f)

    def aggiungi_coperto(self, c):
        self.lista_coperti.append(c)

    def get_coperto(self, i):
        return self.lista_coperti[i]

    def get_lista_coperti(self):
        return self.lista_coperti

    def cancel(self):
        self.lista_coperti = []

    def save_data(self):
        with open("Lista_coperti\\data\\lista_coperti_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_coperti, handle, pickle.HIGHEST_PROTOCOL)