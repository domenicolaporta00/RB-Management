from Lista_ordiniMP.model.lista_ordiniMP_model import lista_ordiniMP_model


class lista_ordiniMP_controller():

    def __init__(self):
        super(lista_ordiniMP_controller, self).__init__()
        self.lordiniMPm = lista_ordiniMP_model()

    def aggiungi_ordineMP(self, ordineMP):
        self.lordiniMPm.aggiungi_ordineMP(ordineMP)

    def get_ordineMP(self, i):
        return self.lordiniMPm.get_ordineMP(i)

    def get_lista_ordiniMP(self):
        return self.lordiniMPm.get_lista_ordiniMP()

    def cancel(self):
        self.lordiniMPm.cancel()

    def elimina(self, ordineMP):
        self.lordiniMPm.elimina(ordineMP)

    def save_data(self):
        self.lordiniMPm.save_data()
