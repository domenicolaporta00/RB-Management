import unittest

from PyQt5.QtCore import QTime

from Lista_prenotazioni.controller.lista_prenotazioni_controller import lista_prenotazioni_controller
from Prenotazioni.controller.prenotazioni_controller import prenotazioni_controller
from Prenotazioni.model.prenotazioni_model import prenotazioni_model


class TestPrenotazioni(unittest.TestCase):

    def setUp(self):
        self.lpc = lista_prenotazioni_controller()
        self.prenotazione = prenotazioni_model('Verdi Giovanni', '5', '13:00', 'un seggiolone', '3456789012', 1)
        self.lpc.aggiungi_prenotazione(self.prenotazione, QTime.fromString(self.prenotazione.orario))
        self.pc = prenotazioni_controller(self.prenotazione)

    def test_inserisci_prenotazione(self):
        self.assertIsNotNone(self.prenotazione)
        self.assertTrue(self.prenotazione in self.lpc.get_lista_prenotazioni())

    def test_ricerca_prenotazione(self):
        self.assertIsNotNone(self.lpc.get_lista_prenotazioni())
        prenotazione_ricercata = self.lpc.get_prenotazione(len(self.lpc.get_lista_prenotazioni()) - 1)
        self.assertTrue(prenotazione_ricercata, self.prenotazione)

    def test_elimina_prenotazione(self):
        self.assertIsNotNone(self.lpc.get_lista_prenotazioni())
        self.pc.set_cognome("Tavolo vuoto!")
        self.pc.set_posti("0")
        self.pc.set_orario("12:00")
        self.pc.set_info("")
        self.pc.set_telefono("")
        eliminata = [self.pc.get_cognome(), self.pc.get_posti(), self.pc.get_orario(), self.pc.get_info(),
                     self.pc.get_telefono(), ]
        self.assertTrue(eliminata, ["Tavolo vuoto!", "0", "12:00", "", ""])


if __name__ == '__main__':
    unittest.main()
