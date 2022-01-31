import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from Costi_covid.view.costi_covid_view import costi_covid_view
from Credenziali.view.VistaCredenziali.VistaCredenziali import VistaCredenziali
from ProgressBar.view.progress_bar_view import progress_bar_view
from Schermata_principale.view.Schermata_principale_view import Schermata_principale_view

if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap("images\\Logo_splash.png"), Qt.WindowStaysOnTopHint)
    splash.show()
    time.sleep(1)
    # vC = VistaCredenziali()
    # vC = Schermata_principale_view("Domenico", "Italiano")
    # vC = costi_covid_view(1, 1)
    vC = progress_bar_view()
    vC.show()
    splash.finish(vC)
    sys.exit(app.exec())
