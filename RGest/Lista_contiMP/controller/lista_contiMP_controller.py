from Lista_contiMP.model.lista_contiMP_model import lista_contiMP_model


class lista_contiMP_controller():

    def __init__(self):
        super(lista_contiMP_controller, self).__init__()
        self.lcMPm = lista_contiMP_model()

    def aggiungi_contoMP(self, conto):
        self.lcMPm.aggiungi_contoMP(conto)

    def get_contoMP(self, index):
        return self.lcMPm.get_contoMP(index)

    def get_lista_contoMP(self):
        return self.lcMPm.get_lista_contoMP()

    def cancel_contoMP(self):
        self.lcMPm.cancel_contoMP()

    def save_data(self):
        self.lcMPm.save_data()
