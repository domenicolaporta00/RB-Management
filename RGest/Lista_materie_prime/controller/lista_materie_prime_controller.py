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

    def get_lista_magazzino(self):
        return self.lmatprimem.get_lista_magazzino()

    def get_mp_inMag(self, i):
        return self.lmatprimem.get_mp_inMag(i)

    def aggiungi_inMag(self, mp):
        self.lmatprimem.aggiungi_inMag(mp)

    def elimina_MP_daMag(self, mp):
        self.lmatprimem.elimina_MP_daMag(mp)

    def cancel_lista_magazzino(self):
        self.lmatprimem.cancel_lista_magazzino()

    def save_data_magazzino(self):
        self.lmatprimem.save_data_magazzino()
