class comanda_controller():

    def __init__(self, comanda_model):
        self.comanda_model = comanda_model

    def get_piatti_list(self):
        return self.comanda_model.piatti_list

    def set_piatti_list(self, lista):
        self.comanda_model.piatti_list = lista
        self.comanda_model.numero = len(lista)

