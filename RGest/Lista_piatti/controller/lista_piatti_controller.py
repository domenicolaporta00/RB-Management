from Lista_piatti.model.lista_piatti_model import lista_piatti_model


class lista_piatti_controller():

    def __init__(self):
        super(lista_piatti_controller, self).__init__()
        self.lpiattim = lista_piatti_model()

    def get_lista_piatti(self):
        return self.lpiattim.get_lista_piatti()

    def get_piatto(self, i):
        return self.lpiattim.get_piatto(i)

    def aggiungi_piatto(self, piatto):
        self.lpiattim.aggiungi_piatto(piatto)

    def save_data(self):
        self.lpiattim.save_data()

    def get_lista_stats(self):
        return self.lpiattim.get_lista_stats()

    def get_stat(self, i):
        return self.lpiattim.get_stat(i)

    def aggiungi_stat(self, stat):
        self.lpiattim.aggiungi_stat(stat)
        print("stat aggiunta")

    def cancel_stats(self):
        self.lpiattim.cancel_stats()

    def save_data_stats(self):
        self.lpiattim.save_data_stats()
