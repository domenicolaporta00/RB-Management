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