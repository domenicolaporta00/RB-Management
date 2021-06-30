from PyQt5.QtCore import QDate


class dipendente_model():
    def __init__(self, cognome, nome, ruolo, postazione, stipendio, telefono, eta):
        self.cognome = cognome
        self.nome = nome
        self.eta = eta
        self.ruolo = ruolo
        self.postazione = postazione
        self.stipendio = stipendio
        self.telefono = telefono
        self.id = cognome[:1]+""+nome[:1]+telefono
        self.data_inizio = self.data = QDate.currentDate().toString("ddd d MMM yyyy")
