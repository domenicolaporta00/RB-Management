class delivery_controller():

    def __init__(self, delivery):
        self.dm = delivery

    def set_cognome(self, cognome):
        self.dm.cognome = cognome

    def set_orario(self, orario):
        self.dm.orario = orario

    def set_telefono(self, telefono):
        self.dm.telefono = telefono

    def set_indirizzo(self, indirizzo):
        self.dm.indirizzo = indirizzo

    def get_cognome(self):
        return self.dm.cognome

    def get_orario(self):
        return self.dm.orario

    def get_telefono(self):
        return self.dm.telefono

    def get_indirizzo(self):
        return self.dm.indirizzo
