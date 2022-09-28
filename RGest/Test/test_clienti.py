import unittest

from Cliente.model.cliente_model import cliente_model
from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller


class TestClienti(unittest.TestCase):

    def setUp(self):
        self.lclientic = lista_clienti_controller()
        self.cliente = cliente_model('Giovanni Neri', '3571234567')
        self.lclientic.aggiungi_cliente(self.cliente)

    def quanti_clienti(self, cliente):
        a = 0
        for p in self.lclientic.get_lista_clienti():
            if (p.nome, p.telefono) == cliente:
                a += 1
        return a

    def test_aggiungi_cliente(self):
        self.assertIsNotNone(self.cliente)
        self.assertTrue(self.cliente in self.lclientic.get_lista_clienti())
        self.assertTrue(self.cliente in self.lclientic.get_lista_clienti_noDoppi())

    def test_aggiorna_cliente(self):
        quantita_prima = self.quanti_clienti((self.cliente.nome, self.cliente.telefono))
        self.lclientic.aggiungi_cliente(self.cliente)
        quantita_dopo = self.quanti_clienti((self.cliente.nome, self.cliente.telefono))
        self.assertEqual(quantita_dopo, quantita_prima + 1)


if __name__ == '__main__':
    unittest.main()
