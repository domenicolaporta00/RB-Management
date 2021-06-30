import json
import os
import pickle

from Materie_prime.model.materie_prime_model import materie_prime_model


class lista_materie_prime_model():

    def __init__(self):
        super(lista_materie_prime_model, self).__init__()
        self.lista_mp = []
        # self.lista_stats = []
        if os.path.isfile('Lista_materie_prime\\data\\lista_mp_salvata.pickle'):
            with open('Lista_materie_prime\\data\\lista_mp_salvata.pickle', 'rb') as f:
                self.lista_mp = pickle.load(f)
        else:
            with open('Lista_materie_prime\\data\\lista_mp_iniziali.json') as f:
                lista_mp_iniziali = json.load(f)
            for mp in lista_mp_iniziali:
                self.aggiungi_mp(materie_prime_model(mp["nome"], mp["prezzo"]))
        '''if os.path.isfile('Lista_piatti\\data\\lista_stats_salvata.pickle'):
            with open('Lista_piatti\\data\\lista_stats_salvata.pickle', 'rb') as F:
                self.lista_stats = pickle.load(F)'''

    def aggiungi_mp(self, mp):
        self.lista_mp.append(mp)

    def get_mp(self, i):
        return self.lista_mp[i]

    def get_lista_mp(self):
        return self.lista_mp

    def save_data(self):
        with open('Lista_materie_prime\\data\\lista_mp_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_mp, handle, pickle.HIGHEST_PROTOCOL)

    '''def aggiungi_stat(self, stat):
        self.lista_stats.append(stat)

    def get_stat(self, i):
        return self.lista_stats[i]

    def get_lista_stats(self):
        return self.lista_stats

    def cancel_stats(self):
        self.lista_stats = []

    def save_data_stats(self):
        with open('Lista_piatti\\data\\lista_stats_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_stats, handle, pickle.HIGHEST_PROTOCOL)'''