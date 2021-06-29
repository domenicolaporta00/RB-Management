class comanda_controller():

    def __init__(self, comanda_model):
        self.comanda_model = comanda_model

    def get_piatti_list(self):
        return self.comanda_model.piatti_list

    '''def get_isDelivery(self):
        return self.comanda_model.isDelivery'''

    '''def get_nome(self):
        return self.comanda_model.nome

    def get_persone(self):
        return self.comanda_model.persone'''

    def set_piatti_list(self, lista):
        self.comanda_model.piatti_list = lista
        self.comanda_model.numero = len(lista)

    '''def set_nome(self, nome):
        self.comanda_model.nome = nome

    def set_persone(self, persone):
        self.comanda_model.persone = persone'''


