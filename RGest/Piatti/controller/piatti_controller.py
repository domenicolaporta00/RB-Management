class piatti_controller():

    def __init__(self, piatto):
        self.piattomodel = piatto

    def get_nome(self):
        return self.piattomodel.nome

    def get_tipo(self):
        return self.piattomodel.tipo

    def get_prezzo(self):
        return self.piattomodel.prezzo
