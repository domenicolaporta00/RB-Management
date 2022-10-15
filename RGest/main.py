import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from ProgressBar.view.progress_bar_view import progress_bar_view

if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = QSplashScreen(QPixmap("images\\Logo_splash.png"), Qt.WindowStaysOnTopHint)
    splash.show()
    time.sleep(1)
    vC = progress_bar_view()
    vC.show()
    splash.finish(vC)
    sys.exit(app.exec())
