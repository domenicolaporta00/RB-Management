import os
import pickle


class lista_clienti_model():

    def __init__(self):
        super(lista_clienti_model, self).__init__()
        self.lista_clienti = []
        if os.path.isfile("Lista_clienti\\data\\lista_clienti_salvata.pickle"):
            with open("Lista_clienti\\data\\lista_clienti_salvata.pickle", "rb") as f:
                self.lista_clienti = pickle.load(f)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def get_cliente(self, i):
        return self.lista_clienti[i]

    def get_lista_clienti(self):
        return self.lista_clienti

    def cancel(self):
        self.lista_clienti = []

    def save_data(self):
        with open("Lista_clienti\\data\\lista_clienti_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)