from Lista_coperti.model.lista_coperti_model import lista_coperti_model


class lista_coperti_controller():

    def __init__(self):
        super(lista_coperti_controller, self).__init__()
        self.lcm = lista_coperti_model()

    def aggiungi_coperto(self, c):
        self.lcm.aggiungi_coperto(c)

    def get_coperto(self, i):
        return self.lcm.get_coperto(i)

    def get_lista_coperti(self):
        return self.lcm.get_lista_coperti()

    def cancel(self):
        self.lcm.cancel()

    def save_data(self):
        self.lcm.save_data()

    def aggiungi_conto(self, conto):
        self.lcm.aggiungi_conto(conto)

    def get_conto(self, index):
        return self.lcm.get_conto(index)

    def get_lista_conto(self):
        return self.lcm.get_lista_conto()

    def cancel_conto(self):
        self.lcm.cancel_conto()

    def save_data_conto(self):
        self.lcm.save_data_conto()

    def aggiungi_consegna(self, consegna):
        self.lcm.aggiungi_consegna(consegna)

    def get_consegna(self, index):
        return self.lcm.get_consegna(index)

    def get_lista_consegne_delivery(self):
        return self.lcm.get_lista_consegne_delivery()

    def cancel_consegne(self):
        self.lcm.cancel_consegne()

    def save_data_delivery(self):
        self.lcm.save_data_delivery()
