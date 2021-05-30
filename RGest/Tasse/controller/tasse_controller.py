class tasse_controller():

    def __init__(self, tasse):
        self.t = tasse

    def get_acqua(self):
        return self.t.acqua

    def get_luce(self):
        return self.t.luce

    def get_gas(self):
        return self.t.gas

    def get_tv(self):
        return self.t.tv

    def get_affitto(self):
        return self.t.affitto