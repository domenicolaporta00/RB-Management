import time
import tkinter.tix

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QProgressBar, QLabel, QPushButton, QComboBox

from Credenziali.view.VistaCredenziali.VistaCredenziali import VistaCredenziali

from tkinter import *

class progress_bar_view(QMainWindow):
    def __init__(self):
        super(progress_bar_view, self).__init__()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 650)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.progressbar = QProgressBar(self)

        self.cb = QComboBox(self)

        self.logo = QLabel(self)

        self.button = QPushButton(self)

        self.schermata()

    def schermata(self):
        pixmax = QPixmap("images\\Logo_definitivo.jpg")
        self.logo.setPixmap(pixmax)
        self.logo.move(225, 50)
        self.logo.setFixedSize(300, 300)

        self.config_button(self.button, "OK", QFont("Times Roman", 11, QFont.Bold), 300, 30, 225, 530)
        self.button.clicked.connect(self.parti)

        self.cb.setFont(QFont("Times Roman", 11))
        self.cb.setFixedSize(300, 30)
        self.cb.move(225, 400)
        self.cb.addItem(QIcon("images\\italia.jpg"), "Italiano")
        self.cb.addItem(QIcon("images\\inglese.png"), "Inglese")

        self.progressbar.setRange(0, 100)
        self.progressbar.setTextVisible(False)
        self.progressbar.move(225, 450)
        self.progressbar.setFixedSize(300, 30)
        self.close()

    def parti(self):
        self.vC = VistaCredenziali(self.cb.currentText())
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


