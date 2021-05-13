class ControllerCredenziali():

    def __init__(self):
        with open("dati di accesso\\prova.txt") as f:
            self.nome = f.read()

        with open("dati di accesso\\prova2.txt") as F:
            self.password = F.read()

    def controllaCredenziali(self, nome, password):
        if nome == self.nome and password == self.password:
            return True

    def aggiornaCredenziali(self, nome, password):
        with open("dati di accesso\\prova.txt", "w") as fl:
            fl.write(nome)
        self.nome = nome
        print(self.nome)

        with open("dati di accesso\\prova2.txt", "w") as Fl:
            Fl.write(password)
        self.password = password
        print(self.password)

    def controlloPassword(self, str):
        if str == self.password:
            return True