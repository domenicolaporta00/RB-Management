from Lista_delivery.model.lista_delivery_model import lista_delivery_model


class lista_delivery_controller():

    def __init__(self):
        super(lista_delivery_controller, self).__init__()
        self.ldm = lista_delivery_model()

    def aggiungi_delivery(self, delivery, orario):
        self.ldm.aggiungi_delivery(delivery, orario)

    def remove_delivery(self, telefono):
        self.ldm.remove_delivery(telefono)

    def remove_delivery_cena(self, telefono):
        self.ldm.remove_delivery_cena(telefono)

    def get_delivery(self, i):
        return self.ldm.get_delivery(i)

    def get_delivery_cena(self, i):
        return self.ldm.get_delivery_cena(i)

    def get_lista_delivery(self):
        return self.ldm.get_lista_delivery()

    def get_lista_delivery_cena(self):
        return self.ldm.get_lista_delivery_cena()

    def cancel(self):
        self.ldm.cancel()

    def cancel_cena(self):
        self.ldm.cancel_cena()

    def save_data(self):
        self.ldm.save_data()
