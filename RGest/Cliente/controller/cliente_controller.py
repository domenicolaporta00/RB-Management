class cliente_controller():
    def __init__(self, cliente):
        self.cliente = cliente

    def get_nome(self):
        return self.cliente.nome

    def get_telefono(self):
        return self.cliente.telefono

    def get_data(self):
        return self.cliente.data
