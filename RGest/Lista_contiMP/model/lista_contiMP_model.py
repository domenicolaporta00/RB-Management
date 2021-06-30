import os
import pickle


class lista_contiMP_model():

    def __init__(self):
        super(lista_contiMP_model, self).__init__()
        self.lista_contiMP = []
        if os.path.isfile("Lista_contiMP\\data\\lista_contiMP_salvata.pickle"):
            with open("Lista_contiMP\\data\\lista_contiMP_salvata.pickle", "rb") as F:
                self.lista_contiMP = pickle.load(F)

    def aggiungi_contoMP(self, conto):
        self.lista_contiMP.append(conto)

    def get_contoMP(self, index):
        return self.lista_contiMP[index]

    def get_lista_contoMP(self):
        return self.lista_contiMP

    def cancel_contoMP(self):
        self.lista_contiMP = []

    def save_data(self):
        with open("Lista_contiMP\\data\\lista_contiMP_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_contiMP, handle, pickle.HIGHEST_PROTOCOL)
