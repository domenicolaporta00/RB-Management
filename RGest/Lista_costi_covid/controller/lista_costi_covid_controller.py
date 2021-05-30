from Lista_costi_covid.model.lista_costi_covid_model import lista_costi_covid_model


class lista_costi_covid_controller():

    def __init__(self):
        super(lista_costi_covid_controller, self).__init__()
        self.lccm = lista_costi_covid_model()

    def aggiungi_covid(self, covid):
        self.lccm.aggiungi_covid(covid)

    def get_covid(self, i):
        return self.lccm.get_covid(i)

    def get_lista_covid(self):
        return self.lccm.get_lista_covid()

    def cancel(self):
        self.lccm.cancel()

    def save_data(self):
        self.lccm.save_data()

