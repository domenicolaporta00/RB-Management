import os
import pickle

from PyQt5.QtCore import QTime


class lista_delivery_model():

    def __init__(self):
        super(lista_delivery_model, self).__init__()
        self.lista_delivery = []
        self.lista_delivery_cena = []
        if os.path.isfile("Lista_delivery\\data\\lista_delivery_salvata.pickle"):
            with open("Lista_delivery\\data\\lista_delivery_salvata.pickle", "rb") as f:
                self.lista_delivery = pickle.load(f)
        if os.path.isfile("Lista_delivery\\data\\lista_delivery_cena_salvata.pickle"):
            with open("Lista_delivery\\data\\lista_delivery_cena_salvata.pickle", "rb") as f:
                self.lista_delivery_cena = pickle.load(f)

    def aggiungi_delivery(self, delivery, orario):
        if QTime(14, 00) >= orario >= QTime(12, 00):
            self.lista_delivery.append(delivery)
        if QTime(22, 00) >= orario >= QTime(19, 00):
            self.lista_delivery_cena.append(delivery)

    def remove_delivery(self, telefono):
        def flag(delivery):
            if delivery.telefono == telefono:
                return True
            return False
        self.lista_delivery.remove(list(filter(flag, self.lista_delivery))[0])

    def remove_delivery_cena(self, telefono):
        def flag(delivery):
            if delivery.telefono == telefono:
                return True
            return False
        self.lista_delivery_cena.remove(list(filter(flag, self.lista_delivery_cena))[0])

    def get_delivery(self, i):
        return self.lista_delivery[i]

    def get_delivery_cena(self, i):
        return self.lista_delivery_cena[i]

    def get_lista_delivery(self):
        return self.lista_delivery

    def get_lista_delivery_cena(self):
        return self.lista_delivery_cena

    def cancel(self):
        self.lista_delivery = []

    def cancel_cena(self):
        self.lista_delivery_cena = []

    def save_data(self):
        with open("Lista_delivery\\data\\lista_delivery_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_delivery, handle, pickle.HIGHEST_PROTOCOL)
        with open("Lista_delivery\\data\\lista_delivery_cena_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_delivery_cena, handle, pickle.HIGHEST_PROTOCOL)