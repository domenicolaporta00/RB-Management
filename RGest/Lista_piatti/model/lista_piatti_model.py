import os
import pickle
import json

from Piatti.model.piatti_model import piatti_model


class lista_piatti_model():

    def __init__(self):
        super(lista_piatti_model, self).__init__()
        self.lista_piatti = []
        if os.path.isfile('Lista_piatti\\data\\lista_piatti_salvata.pickle'):
            with open('Lista_piatti\\data\\lista_piatti_salvata.pickle', 'rb') as f:
                self.lista_piatti = pickle.load(f)
        else:
            with open('Lista_piatti\\data\\lista_piatti_iniziali.json') as f:
                lista_piatti_iniziali = json.load(f)
            for piatto in lista_piatti_iniziali:
                self.aggiungi_piatto(piatti_model(piatto["nome"], piatto["tipo"], piatto["prezzo"]))

    def aggiungi_piatto(self, piatto):
        self.lista_piatti.append(piatto)

    def get_piatto(self, i):
        return self.lista_piatti[i]

    def get_lista_piatti(self):
        return self.lista_piatti

    def save_data(self):
        with open('Lista_piatti\\data\\lista_piatti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_piatti, handle, pickle.HIGHEST_PROTOCOL)
