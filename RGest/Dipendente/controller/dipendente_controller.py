class dipendente_controller():

    def __init__(self, dipendente):
        self.dm = dipendente

    def set_cognome(self, cognome):
        self.dm.cognome = cognome

    def set_nome(self, nome):
        self.dm.nome = nome

    def set_ruolo(self, ruolo):
        self.dm.ruolo = ruolo

    def set_postazione(self, postazione):
        self.dm.postazione = postazione

    def set_stipendio(self, stipendio):
        self.dm.stipendio = stipendio

    def set_telefono(self, telefono):
        self.dm.telefono = telefono

    def set_eta(self, eta):
        self.dm.eta = eta

    def set_id(self, id):
        self.dm.id = id

    def set_data_inizio(self, di):
        self.dm.data_inizio = di

    def get_cognome(self):
        return self.dm.cognome

    def get_nome(self):
        return self.dm.nome

    def get_ruolo(self):
        return self.dm.ruolo

    def get_postazione(self):
        return self.dm.postazione

    def get_stipendio(self):
        return self.dm.stipendio

    def get_telefono(self):
        return self.dm.telefono

    def get_eta(self):
        return self.dm.eta

    def get_id(self):
        return self.dm.id

    def get_data_inizio(self):
        return self.dm.data_inizio
