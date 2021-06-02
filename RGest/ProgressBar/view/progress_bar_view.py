import time

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QProgressBar, QLabel, QPushButton, QBoxLayout, QVBoxLayout, QWidget

from Credenziali.view.VistaCredenziali.VistaCredenziali import VistaCredenziali


class progress_bar_view(QMainWindow):
    def __init__(self):
        super(progress_bar_view, self).__init__()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.vC = VistaCredenziali()

        self.progressbar = QProgressBar(self)

        self.logo = QLabel(self)

        self.button = QPushButton(self)

        self.schermata()

    def schermata(self):
        pixmax = QPixmap("images\\Logo_definitivo.jpg")

        self.logo.setPixmap(pixmax)
        self.logo.move(225, 100)
        self.logo.setFixedSize(300, 300)

        self.config_button(self.button, "Avvia app", QFont("Times Roman", 11, QFont.Bold), 300, 30, 225, 530)
        self.button.clicked.connect(self.parti)

        self.progressbar.setRange(0, 100)
        self.progressbar.setTextVisible(False)
        self.progressbar.move(225, 450)
        self.progressbar.setFixedSize(300, 30)
        #self.progressbar.show()
        self.close()

    def parti(self):
        maximum = self.progressbar.maximum()
        for n in range(maximum + 1):
            time.sleep(0.02)
            self.progressbar.setValue(n)
        time.sleep(1)
        self.vC.show()
        self.close()

    def config_button(self, button, text, font, a, b, x, y):
        button.setText(text)
        button.setFont(font)
        button.move(x, y)
        button.setFixedSize(a, b)
        button.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")


