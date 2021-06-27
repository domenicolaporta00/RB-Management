class consegna_delivery_controller():

    def __init__(self, cdc):
        self.cdc = cdc

    def get_numero(self):
        return self.cdc.data

    def get_data(self):
        return self.cdc.ricavo_tot

    def get_n(self):
        return self.cdc.n
