class materie_prime_controller():

    def __init__(self, mp):
        self.mp = mp

    def get_nome(self):
        return self.mp.nome

    def get_prezzo(self):
        return self.mp.prezzo
