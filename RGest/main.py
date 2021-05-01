import sys
from PyQt5.QtWidgets import QApplication

from Credenziali.view.VistaCredenziali.VistaCredenziali import VistaCredenziali

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vC = VistaCredenziali()
    #vC = Schermata_principale_view()
    vC.show()
    sys.exit(app.exec())
