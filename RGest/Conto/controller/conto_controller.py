class conto_controller():

    def __init__(self, cm):
        self.cm = cm

    def get_data(self):
        return self.cm.data

    def get_conto(self):
        return self.cm.conto

    def get_orario(self):
        return self.cm.orario
