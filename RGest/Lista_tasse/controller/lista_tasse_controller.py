from Lista_tasse.model.lista_tasse_model import lista_tasse_model


class lista_tasse_controller():

    def __init__(self):
        super(lista_tasse_controller, self).__init__()
        self.ltm = lista_tasse_model()

    def aggiungi_tasse(self, tax):
        self.ltm.aggiungi_tasse(tax)

    def get_tax(self, i):
        return self.ltm.get_tax(i)

    def get_lista_tasse(self):
        return self.ltm.get_lista_tasse()

    def cancel(self):
        self.ltm.cancel()

    def save_data(self):
        self.ltm.save_data()
