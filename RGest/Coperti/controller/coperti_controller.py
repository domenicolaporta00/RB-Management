class coperti_controller():

    def __init__(self, cm):
        self.cm = cm

    def get_numero(self):
        return self.cm.n

    def get_data(self):
        return self.cm.data

    def get_ricavo_tot(self):
        return self.cm.ricavo_tot
