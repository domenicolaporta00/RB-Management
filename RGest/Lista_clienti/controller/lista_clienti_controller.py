from Lista_clienti.model.lista_clienti_model import lista_clienti_model


class lista_clienti_controller():

    def __init__(self):
        super(lista_clienti_controller, self).__init__()
        self.lcm = lista_clienti_model()

    def aggiungi_cliente(self, cliente):
        self.lcm.aggiungi_cliente(cliente)

    def get_cliente(self, i):
        return self.lcm.get_cliente(i)

    def get_lista_clienti(self):
        return self.lcm.get_lista_clienti()

    def cancel(self):
        self.lcm.cancel()

    def save_data(self):
        self.lcm.save_data()