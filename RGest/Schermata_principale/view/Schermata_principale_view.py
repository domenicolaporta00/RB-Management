import webbrowser

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenu

from Costi.view.costi_view import costi_view
from Costi_covid.view.costi_covid_view import costi_covid_view
from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller
from Lista_dipendenti.view.lista_dipendenti_view import lista_dipendenti_view
from Lista_prenotazioni.view.lista_prenotazioni_view import lista_prenotazioni_view
from Lista_tasse.controller.lista_tasse_controller import lista_tasse_controller
from Tasse.view.tasse_view import tasse_view


class Schermata_principale_view(QMainWindow):
    def __init__(self):
        super(Schermata_principale_view, self).__init__()

        self.lpv = lista_prenotazioni_view()
        self.ldv = lista_dipendenti_view()
        self.lccc = lista_costi_covid_controller()
        self.ltc = lista_tasse_controller()
        #self.ccv = costi_covid_view(self.lccc)
        #self.cv = costi_view()

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.serviziButton = QPushButton(self)
        self.magazzinoButton = QPushButton(self)
        self.backofficeButton = QPushButton(self)
        self.datiButton = QPushButton(self)
        self.infoCovidButton = QPushButton(self)
        self.deliveryButton = QPushButton(self)
        self.sviluppatori = QPushButton(self)

        self.selezionare = QLabel(self)
        self.logo = QLabel(self)
        self.servizi = QLabel(self)
        self.magazzino = QLabel(self)
        self.backoffice = QLabel(self)
        self.dati = QLabel(self)
        self.infoCovid = QLabel(self)
        self.delivery = QLabel(self)

        self.schermata()

    def schermata(self):
        font = QFont("Times Roman", 11, QFont.Bold)
        menu = QMenu()
        menu.addAction("Prenotazioni                 ", self.prenotazioni)
        menu.addAction("Comanda")
        menu.addAction("Conto")

        menu2 = QMenu()
        menu2.addAction("Magazzino standard")
        menu2.addAction("Magazzino gluten-free")

        menu3 = QMenu()
        menu3.addAction("Gestione personale      ", self.dipendenti)
        menu3.addAction("Tasse", self.tasse)
        menu3.addAction("Costi", self.costi)
        menu3.addAction("Guadagni")

        menuS = QMenu()
        menuS.addAction("Ciccolini Joshua            ", self.cj)
        menuS.addAction("Colleluori Davide", self.cd)
        menuS.addAction("La Porta Domenico", self.dlp)

        menuCovid = QMenu()
        menuCovid.addAction("Visita il sito del Governo", self.governo)
        menuCovid.addAction("Controlla i colori delle regioni", self.colori)
        menuCovid.addAction("Elenco buone norme da seguire", self.norme)
        menuCovid.addAction("Andamento Covid", self.andamento)
        menuCovid.addAction("Ordine prodotti", self.costi_covid)

        str = "images\\"

        servizioPixmap = QPixmap(str+"servizio.png")
        magazzinoPixmap = QPixmap(str+"magazzino.png")
        backofficePixmap = QPixmap(str+"backoffice.png")
        datiPixmap = QPixmap(str+"dati.png")
        infocovidPixmap = QPixmap(str+"covid.png")
        deliveryPixmap = QPixmap(str+"delivery.png")
        LogoPixmax = QPixmap(str+"Logo_tagliato.png")

        self.selezionare.setText("                 Benvenuto in RGest. \nPrego, selezionare un'opzione dal menù:")
        self.selezionare.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.selezionare.setStyleSheet("color: red")
        self.selezionare.move(100, 50)
        self.selezionare.setFixedSize(750, 100)

        self.serviziButton.move(175, 175)
        self.serviziButton.setText("Gestione servizi")
        self.serviziButton.setFont(font)
        self.serviziButton.setFixedSize(175, 50)
        self.serviziButton.setMenu(menu)
        self.serviziButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.magazzinoButton.move(175, 300)
        self.magazzinoButton.setText("Gestione magazzino")
        self.magazzinoButton.setFont(font)
        self.magazzinoButton.setFixedSize(175, 50)
        self.magazzinoButton.setMenu(menu2)
        self.magazzinoButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.backofficeButton.move(175, 425)
        self.backofficeButton.setText("Gestione backoffice")
        self.backofficeButton.setFont(font)
        self.backofficeButton.setFixedSize(175, 50)
        self.backofficeButton.setMenu(menu3)
        self.backofficeButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.datiButton.move(400, 175)
        self.datiButton.setText("Dati")
        self.datiButton.setFont(font)
        self.datiButton.setFixedSize(175, 50)
        self.datiButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.infoCovidButton.move(400, 300)
        self.infoCovidButton.setText("Info Covid")
        self.infoCovidButton.setFont(font)
        self.infoCovidButton.setFixedSize(175, 50)
        self.infoCovidButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.infoCovidButton.setMenu(menuCovid)

        self.deliveryButton.move(400, 425)
        self.deliveryButton.setText("Gestione delivery")
        self.deliveryButton.setFont(font)
        self.deliveryButton.setFixedSize(175, 50)
        self.deliveryButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.logo.setPixmap(LogoPixmax)
        self.logo.setFixedSize(110, 110)
        self.logo.move(200, 500)

        self.sviluppatori.setText("Info sviluppatori")
        self.sviluppatori.move(400, 525)
        self.sviluppatori.setFont(font)
        self.sviluppatori.setFixedSize(175, 50)
        self.sviluppatori.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.sviluppatori.setMenu(menuS)

        self.config_foto(self.servizi, servizioPixmap, 50, 150, 110, 100)

        self.config_foto(self.magazzino, magazzinoPixmap, 50, 275, 110, 100)

        self.config_foto(self.backoffice, backofficePixmap, 50, 400, 110, 100)

        self.config_foto(self.dati, datiPixmap, 600, 150, 110, 100)

        self.config_foto(self.infoCovid, infocovidPixmap, 600, 275, 110, 100)

        self.config_foto(self.delivery, deliveryPixmap, 600, 400, 110, 100)

    def config_foto(self, layout, pixmap, x, y, a, b):
        layout.setPixmap(pixmap)
        layout.move(x, y)
        layout.setFixedSize(a, b)

    def dlp(self):
        url = "https://www.instagram.com/dominik_laporta00/"
        webbrowser.open(url)

    def cj(self):
        url = "https://www.instagram.com/joshuaciccolini/"
        webbrowser.open(url)

    def cd(self):
        url = "https://www.instagram.com/davidecolleluori/"
        webbrowser.open(url)

    def governo(self):
        url = "http://www.salute.gov.it/portale/nuovocoronavirus/homeNuovoCoronavirus.jsp"
        webbrowser.open(url)

    def colori(self):
        url = "https://www.governo.it/it/articolo/domande-frequenti-sulle-misure-adottate-dal-governo/15638?gclid=Cj0KCQjw1a6EBhC0ARIsAOiTkrHiNT9HVBO_fV6CbZ0OFop6M6gIaLEctgsFv79OR6XKw--NdNlDRG4aAprHEALw_wcB"
        webbrowser.open(url)

    def norme(self):
        url = "https://www.governo.it/it/coronavirus-dieci-regole"
        webbrowser.open(url)

    def andamento(self):
        url = "https://www.google.com/search?q=coronavirus&sxsrf=ALeKk00h4z0EaEa1GwW2hezYhnhXnzm0oA%3A1619795169950&ei=4RyMYMK0OYOWkwX5s5eQDQ&oq=coron&gs_lcp=Cgdnd3Mtd2l6EAMYADIHCCMQyQMQJzIFCAAQkgMyBQgAEJIDMgQIIxAnMgQIIxAnMgQIABBDMgQIABBDMggIABCxAxCDATIICAAQsQMQgwEyBAgAEEM6AggAOgoIABCxAxCDARBDUMIfWLkkYMIraABwAHgAgAGbAYgBzgWSAQMxLjWYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=gws-wiz#wptab=s:H4sIAAAAAAAAAONgVuLVT9c3NMwySk6OL8zJecTozS3w8sc9YSmnSWtOXmO04eIKzsgvd80rySypFNLjYoOyVLgEpVB1ajBI8XOhCvHsYuL2SE3MKckILkksKV7EKl0MpDOLSzKTM1IViktzFJLzi_LzEssyi0qLAQ16CwOLAAAA"
        webbrowser.open(url)

    def prenotazioni(self):
        self.lpv.show()

    def dipendenti(self):
        self.ldv.show()

    def costi_covid(self):
        self.ccv = costi_covid_view(self.lccc)
        self.ccv.show()

    def tasse(self):
        self.tv = tasse_view(self.ltc)
        self.tv.show()

    def costi(self):
        self.cv = costi_view()
        self.cv.show()

