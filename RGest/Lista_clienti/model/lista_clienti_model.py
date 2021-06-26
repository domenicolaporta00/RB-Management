import os
import pickle


class lista_clienti_model():

    def __init__(self):
        super(lista_clienti_model, self).__init__()
        self.lista_clienti = []
        self.lista_clienti_noDoppi = []
        if os.path.isfile("Lista_clienti\\data\\lista_clienti_salvata.pickle"):
            with open("Lista_clienti\\data\\lista_clienti_salvata.pickle", "rb") as f:
                self.lista_clienti = pickle.load(f)
        if os.path.isfile("Lista_clienti\\data\\lista_clienti_nD_salvata.pickle"):
            with open("Lista_clienti\\data\\lista_clienti_nD_salvata.pickle", "rb") as F:
                self.lista_clienti_noDoppi = pickle.load(F)

    def aggiungi_cliente(self, cliente):
        self.lista_clienti.append(cliente)

    def get_cliente(self, i):
        return self.lista_clienti[i]

    def get_lista_clienti(self):
        return self.lista_clienti

    def get_lista_clienti_noDoppi(self):
        for cliente in self.get_lista_clienti():
            if self.controllo(cliente):
                pass
            else:
                self.lista_clienti_noDoppi.append(cliente)
                pass
        return self.lista_clienti_noDoppi

    def cancel(self):
        self.lista_clienti = []

    def cancel_noDoppi(self):
        self.lista_clienti_noDoppi = []

    def save_data(self):
        with open("Lista_clienti\\data\\lista_clienti_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_clienti, handle, pickle.HIGHEST_PROTOCOL)
        with open("Lista_clienti\\data\\lista_clienti_nD_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_clienti_noDoppi, handle, pickle.HIGHEST_PROTOCOL)

    def controllo(self, c):
        for cliente in self.lista_clienti_noDoppi:
            if c.nome == cliente.nome and c.telefono == cliente.telefono:
                return True
        return False
