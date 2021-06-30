class ordineMP_controller():

    def __init__(self, ordineMP_model):
        self.ordineMP_model = ordineMP_model

    def get_mp_list(self):
        return self.ordineMP_model.mp_list

    def set_mp_list(self, lista):
        self.ordineMP_model.mp_list = lista
        self.ordineMP_model.numero = len(lista)
