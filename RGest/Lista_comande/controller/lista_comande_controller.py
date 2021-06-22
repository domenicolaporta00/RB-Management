from Lista_comande.model.lista_comande_model import lista_comande_model


class lista_comande_controller():

    def __init__(self):
        super(lista_comande_controller, self).__init__()
        self.lcomandem = lista_comande_model()

    def aggiungi_comanda(self, comanda):
        self.lcomandem.aggiungi_comanda(comanda)

    def get_comanda(self, i):
        return self.lcomandem.get_comanda(i)

    def get_lista_comande(self):
        return self.lcomandem.get_lista_comande()

    def cancel(self):
        self.lcomandem.cancel()

    def save_data(self):
        self.lcomandem.save_data()