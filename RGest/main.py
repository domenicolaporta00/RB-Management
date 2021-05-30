import sys
import os
from PyQt5.QtWidgets import QApplication

from Costi_covid.view.costi_covid_view import costi_covid_view
from Credenziali.view.VistaCredenziali.VistaCredenziali import VistaCredenziali
from Schermata_principale.view.Schermata_principale_view import Schermata_principale_view

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #vC = VistaCredenziali()
    vC = Schermata_principale_view()
    #vC = costi_covid_view(1, 1)
    vC.show()
    sys.exit(app.exec())
