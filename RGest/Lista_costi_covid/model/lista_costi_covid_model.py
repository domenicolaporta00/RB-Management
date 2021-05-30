import os
import pickle

class lista_costi_covid_model():

    def __init__(self):
        super(lista_costi_covid_model, self).__init__()
        self.lista_covid = []
        if os.path.isfile("Lista_costi_covid\\data\\lista_covid_salvata.pickle"):
            with open("Lista_costi_covid\\data\\lista_covid_salvata.pickle", "rb") as f:
                self.lista_covid = pickle.load(f)

    def aggiungi_covid(self, covid):
        self.lista_covid.append(covid)

    def get_covid(self, i):
        return self.lista_covid[i]

    def get_lista_covid(self):
        return self.lista_covid

    def cancel(self):
        self.lista_covid = []

    def save_data(self):
        with open("Lista_costi_covid\\data\\lista_covid_salvata.pickle", "wb") as handle:
            pickle.dump(self.lista_covid, handle, pickle.HIGHEST_PROTOCOL)