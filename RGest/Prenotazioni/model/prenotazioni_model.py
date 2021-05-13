class prenotazioni_model():

    def __init__(self, cognome, posti, orario, info, telefono, tavolo):
        super(prenotazioni_model, self).__init__()
        self.cognome = cognome
        self.posti = posti
        self.orario = orario
        self.info = info
        self.telefono = telefono
        self.tavolo = tavolo