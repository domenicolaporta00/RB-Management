import unittest

from Dipendente.model.dipendente_model import dipendente_model
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller


class TestDipendenti(unittest.TestCase):

    def setUp(self):
        self.ldc = lista_dipendenti_controller()
        self.dipendente = dipendente_model('Rossi', 'Marco', 'Chef', 'Cucina', '2000', '3334455678', '30')
        self.ldc.aggiungi_dipendente(self.dipendente)

    def test_inserisci_dipendente(self):
        self.assertIsNotNone(self.dipendente)
        self.assertTrue(self.dipendente in self.ldc.get_lista_dipendenti())

    def test_ricerca_dipendente(self):
        self.assertIsNotNone(self.ldc.get_lista_dipendenti())
        dip = self.ldc.get_dipendente(len(self.ldc.get_lista_dipendenti())-1)
        self.assertTrue(dip, self.dipendente)

    def test_elimina_dipendente(self):
        self.assertIsNotNone(self.ldc.get_lista_dipendenti())
        self.ldc.remove_dipendente(self.dipendente.id)
        self.assertTrue(self.dipendente not in self.ldc.get_lista_dipendenti())


if __name__ == '__main__':
    unittest.main()
