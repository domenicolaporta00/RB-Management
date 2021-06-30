from Lista_materie_prime.model.lista_materie_prime_model import lista_materie_prime_model


class lista_materie_prime_controller():

    def __init__(self):
        super(lista_materie_prime_controller, self).__init__()
        self.lmatprimem = lista_materie_prime_model()

    def get_lista_mp(self):
        return self.lmatprimem.get_lista_mp()

    def get_mp(self, i):
        return self.lmatprimem.get_mp(i)

    def aggiungi_mp(self, mp):
        self.lmatprimem.aggiungi_mp(mp)

    def save_data(self):
        self.lmatprimem.save_data()

    '''def get_lista_stats(self):
        return self.lpiattim.get_lista_stats()

    def get_stat(self, i):
        return self.lpiattim.get_stat(i)

    def aggiungi_stat(self, stat):
        self.lpiattim.aggiungi_stat(stat)

    def cancel_stats(self):
        self.lpiattim.cancel_stats()

    def save_data_stats(self):
        self.lpiattim.save_data_stats()'''