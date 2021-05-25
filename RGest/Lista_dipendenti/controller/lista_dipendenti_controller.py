from Lista_dipendenti.model.lista_dipendenti_model import lista_dipendenti_model

class lista_dipendenti_controller:

    def __init__(self):
        super(lista_dipendenti_controller, self).__init__()
        self.ldm = lista_dipendenti_model()

    def aggiungi_dipendente(self, dipendente):
        self.ldm.aggiungi_dipendente(dipendente)

    def get_dipendente(self, i):
        return self.ldm.get_dipendente(i)

    def get_lista_dipendenti(self):
        return self.ldm.get_lista_dipendenti()

    def remove_dipendente(self, id):
        self.ldm.remove_dipendente(id)

    def cancel(self):
        self.ldm.cancel()

    def save_data(self):
        self.ldm.save_data()