import os
import webbrowser

import matplotlib.pyplot as p
import numpy as np
import pywhatkit
from PyQt5.QtCore import QTime, QDate
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMenu, QAction, QMessageBox, QInputDialog
from gtts import gTTS
from playsound import playsound

from Costi.view.costi_view import costi_view
from Costi_covid.view.costi_covid_view import costi_covid_view
from Guadagni.view.guadagni_view import guadagni_view
from Lista_clienti.controller.lista_clienti_controller import lista_clienti_controller
from Lista_clienti.view.lista_clienti_view import lista_clienti_view
from Lista_comande.view.lista_comande_view import lista_comande_view
from Lista_costi_covid.controller.lista_costi_covid_controller import lista_costi_covid_controller
from Lista_delivery.view.lista_delivery_view import lista_delivery_view
from Lista_dipendenti.controller.lista_dipendenti_controller import lista_dipendenti_controller
from Lista_dipendenti.view.lista_dipendenti_view import lista_dipendenti_view
from Lista_ordiniMP.view.consumoMP_view import consumoMP_view
from Lista_ordiniMP.view.lista_ordiniMP_view import lista_ordiniMP_view
from Lista_ordiniMP.view.magazzino_view import magazzino_view
from Lista_piatti.controller.lista_piatti_controller import lista_piatti_controller
from Lista_prenotazioni.view.lista_prenotazioni_view import lista_prenotazioni_view
from Lista_tasse.controller.lista_tasse_controller import lista_tasse_controller
from Tasse.view.tasse_view import tasse_view


class Schermata_principale_view(QMainWindow):
    def __init__(self, nome, lingua):
        global str41, str21, str51, str31
        super(Schermata_principale_view, self).__init__()

        self.lingua = lingua

        if self.lingua == "Inglese":
            str21 = "Contacts"
            str31 = "Contact employees"
            str41 = "Clock"
            str51 = "Time and date"
        elif self.lingua == "Italiano":
            str21 = "Contatti"
            str31 = "Contatta dipendenti"
            str41 = "Orologio"
            str51 = "Ora e data"

        self.lpv = lista_prenotazioni_view(lingua)
        self.ldv = lista_dipendenti_view(lingua)
        self.lcomandav_noDelivery = lista_comande_view(False, lingua)
        self.lcomandav_Delivery = lista_comande_view(True, lingua)
        self.lccc = lista_costi_covid_controller()
        self.ltc = lista_tasse_controller()

        self.nome = nome

        self.icona = QIcon("images\\Logo_definitivo.jpg")

        self.setGeometry(300, 50, 750, 500)
        self.setWindowTitle("RGest")
        self.setFixedSize(750, 650)
        self.setWindowIcon(self.icona)
        self.setStyleSheet("background-color: rgb(230, 230, 230)")

        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.config_menubar("File", QIcon("images\\exit.png"), "Exit", 'Ctrl+Q').triggered.connect(self.close)
        self.config_menubar("Info", QIcon("images\\pint.jpg"), "Tutorial", 'Ctrl+W').triggered.connect(self.tutorial)
        self.config_menubar(str21, QIcon("images\\telefono.png"), str31,
                            "Ctrl+E").triggered.connect(self.contatti)
        self.config_menubar(str41, QIcon("images\\orologio.jpg"), str51, 'Ctrl+R').triggered.connect(
            self.data_ora)

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

        global str26, str25, str24, str23, str22, str21, str20, str19, str18, str17, str16, str15, str14, str13, str12, str11, str10, str9, str8, str7, str6, str5, str4, str1, str2, str3
        if self.lingua == "Inglese":
            str1 = "Warehouse"
            str2 = "Booking"
            str3 = "Commands"
            str4 = "Order raw materials"
            str5 = "Consumption of raw materials"
            str6 = "Personal management"
            str7 = "Taxes"
            str8 = "Costs"
            str9 = "Earnings"
            str10 = "Customer list"
            str11 = "Best selling dishes statistics"
            str12 = "Customers more present"
            str13 = "Government website"
            str14 = "Colors of the regions"
            str15 = "Good rules to follow"
            str16 = "Covid trend"
            str17 = "Order products"
            str18 = "Calls"
            str19 = "Orders"
            str20 = "                 Welcome in RGest. \nPlease select an option from the menu:"
            str21 = "Service MGMT"
            str22 = "Warehouse MGMT"
            str23 = "Backoffice MGMT"
            str24 = "Data"
            str25 = "Delivery MGMT"
            str26 = "Developer info"
        elif self.lingua == "Italiano":
            str1 = "Magazzino"
            str2 = "Prenotazione"
            str3 = "Comanda"
            str4 = "Ordine materie prime"
            str5 = "Consumo materie prime"
            str6 = "Gestione personale"
            str7 = "Tasse"
            str8 = "Costi"
            str9 = "Guadagni"
            str10 = "Lista clienti"
            str11 = "Lista piatti più venduti"
            str12 = "Clienti più presenti"
            str13 = "Sito del governo"
            str14 = "Colori delle regioni"
            str15 = "Buone regole da seguire"
            str16 = "Andamento covid"
            str17 = "Ordine prodotti"
            str18 = "Chiamate"
            str19 = "Ordini"
            str20 = "                 Benvenuto in RGest. \nPrego selezionare un opzione dal menù:"
            str21 = "Gestione servizi"
            str22 = "Gestione magazzino"
            str23 = "Gestione backoffice"
            str24 = "Dati"
            str25 = "Gestione delivery"
            str26 = "Info sviluppatori"

        font = QFont("Times Roman", 11, QFont.Bold)
        menu = QMenu()
        menu.addAction(str2, self.prenotazioni)
        menu.addAction(str3, self.comanda)

        menu2 = QMenu()
        menu2.addAction(str1, self.magazzino_click)
        menu2.addAction(str4, self.ordine_materie)
        menu2.addAction(str5, self.consumo_materie)

        menu3 = QMenu()
        menu3.addAction(str6, self.dipendenti)
        menu3.addAction(str7, self.tasse)
        menu3.addAction(str8, self.costi)
        menu3.addAction(str9, self.guadagni)

        menuS = QMenu()
        menuS.addAction("Ciccolini Joshua            ", self.cj)
        menuS.addAction("Colleluori Davide", self.cd)
        menuS.addAction("La Porta Domenico", self.dlp)

        menuDati = QMenu()
        menuDati.addAction(str10, self.dati_clienti)
        menuDati.addAction(str11, self.grafico)
        menuDati.addAction(str12, self.grafico_clienti)

        menuCovid = QMenu()
        menuCovid.addAction(str13, self.governo)
        menuCovid.addAction(str14, self.colori)
        menuCovid.addAction(str15, self.norme)
        menuCovid.addAction(str16, self.andamento)
        menuCovid.addAction(str17, self.costi_covid)

        menuDelivery = QMenu()
        menuDelivery.addAction(str18, self.chiamate)
        menuDelivery.addAction(str19, self.comandaDelivery)

        str = "images\\"

        servizioPixmap = QPixmap(str + "servizio.png")
        magazzinoPixmap = QPixmap(str + "magazzino.png")
        backofficePixmap = QPixmap(str + "backoffice.png")
        datiPixmap = QPixmap(str + "dati.png")
        infocovidPixmap = QPixmap(str + "covid.png")
        deliveryPixmap = QPixmap(str + "delivery.png")
        LogoPixmax = QPixmap(str + "Logo_tagliato.png")

        self.selezionare.setText(str20)
        self.selezionare.setFont(QFont("Times Roman", 20, QFont.Bold))
        self.selezionare.setStyleSheet("color: red")
        self.selezionare.move(100, 50)
        self.selezionare.setFixedSize(750, 100)

        self.serviziButton.move(175, 175)
        self.serviziButton.setText(str21)
        self.serviziButton.setFont(font)
        self.serviziButton.setFixedSize(175, 50)
        self.serviziButton.setMenu(menu)
        self.serviziButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.magazzinoButton.move(175, 300)
        self.magazzinoButton.setText(str22)
        self.magazzinoButton.setFont(font)
        self.magazzinoButton.setFixedSize(175, 50)
        self.magazzinoButton.setMenu(menu2)
        self.magazzinoButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.backofficeButton.move(175, 425)
        self.backofficeButton.setText(str23)
        self.backofficeButton.setFont(font)
        self.backofficeButton.setFixedSize(175, 50)
        self.backofficeButton.setMenu(menu3)
        self.backofficeButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.datiButton.move(400, 175)
        self.datiButton.setText(str24)
        self.datiButton.setFont(font)
        self.datiButton.setFixedSize(175, 50)
        self.datiButton.setMenu(menuDati)
        self.datiButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.infoCovidButton.move(400, 300)
        self.infoCovidButton.setText("Info Covid")
        self.infoCovidButton.setFont(font)
        self.infoCovidButton.setFixedSize(175, 50)
        self.infoCovidButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.infoCovidButton.setMenu(menuCovid)

        self.deliveryButton.move(400, 425)
        self.deliveryButton.setText(str25)
        self.deliveryButton.setFont(font)
        self.deliveryButton.setFixedSize(175, 50)
        self.deliveryButton.setMenu(menuDelivery)
        self.deliveryButton.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")

        self.logo.setPixmap(LogoPixmax)
        self.logo.setFixedSize(110, 110)
        self.logo.move(200, 500)

        self.sviluppatori.setText(str26)
        self.sviluppatori.move(400, 525)
        self.sviluppatori.setFont(font)
        self.sviluppatori.setFixedSize(175, 50)
        self.sviluppatori.setStyleSheet("background-color: red; border-radius: 10px; color: rgb(255, 255, 255)")
        self.sviluppatori.setMenu(menuS)

        self.config_foto(self.servizi, servizioPixmap, 50, 150, 110, 110)

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

    def config_menubar(self, str, img, _str2, tasti):
        self.menu_def = self.menu_bar.addMenu(str)
        icon = QIcon(img)
        action = QAction(icon, _str2, parent=self)
        action.setShortcut(tasti)
        # action.setStatusTip('Exit application')
        # action.triggered.connect(funzione)
        self.menu_def.addAction(action)
        return action

    def tutorial(self):
        print("Tutorial da fare")

    def data_ora(self):

        global language, str1_
        oggi = QDate.currentDate().toString("dddd d MMMM yyyy")
        ora = QTime.currentTime().toString("hh:mm")
        if self.lingua == "Inglese":
            language = "en"
            str1_ = "Hello " + self.nome + " it's " + ora + " on " + oggi
        if self.lingua == "Italiano":
            language = "it"
            str1_ = "Ciao " + self.nome + " sono le " + ora + " di " + oggi

        audio = "speech.mp3"
        sp = gTTS(text=str1_, lang=language, slow=False)
        sp.save(audio)
        playsound(audio)
        os.remove(audio)

    def contatti(self):

        global str50, str40, str30, str20_, str10_
        if self.lingua == "Inglese":
            str10_ = "Empty employee list. Unable to send messages."
            str20_ = "Write your message. (Warning! The procedure can take\na long time and cannot be done" \
                   "in the background.\nIt is recommended to run outside business hours!\nPress ok to" \
                   "to continue!) "
            str30 = "Type something!"
            str40 = "The system will open whatsapp web for each employee stored and there will be twenty seconds to" \
                   "provision to frame the QR code; at the end of twenty seconds the message will be sent" \
                   "correctly and you will go to the next one. Do not interact with the application while sending the" \
                   "messages! "
            str50 = "Sending messages finished."
        if self.lingua == "Italiano":
            str10_ = "Lista dipendenti vuota. Impossibile inviare messaggi."
            str20_ = "Scrivi il messaggio. (Attenzione! La procedura può impiegare\ntanto tempo e non può essere fatta " \
                   "in background.\nSi consiglia di eseguire fuori dall'orario lavorativo!\nPremere ok per " \
                   "continuare!) "
            str30 = "Digitare qualcosa!"
            str40 = "Il sistema aprirà whatsapp web per ogni dipendente memorizzato e ci saranno venti secondi a " \
                   "disposizione per inquadrare il QR code; al termine dei venti secondi il messaggio verrà inviato " \
                   "correttamente e si passerà al successivo. Non interagire con l'applicazione durante l'invio dei " \
                   "messaggi! "
            str50 = "Invio messaggi terminato."

        self.ldc = lista_dipendenti_controller()
        if not self.ldc.get_lista_dipendenti():
            QMessageBox.warning(None, "RGest", str10_)
        else:
            text, select = QInputDialog.getText(None, "RGest", str20_)
            if not select:
                pass
            else:
                if not text:
                    QMessageBox.warning(None, "RGest", str30)
                else:
                    QMessageBox.warning(None, "RGest", str40)
                    for dipendente in self.ldc.get_lista_dipendenti():
                        ora = QTime.currentTime().hour()
                        minuto = QTime.currentTime().minute() + 1
                        if minuto == 60:
                            minuto = 0
                            ora += 1
                        else:
                            mex = "Car* " + dipendente.nome + ", " + text
                            # print("Invio " + mex + " a " + dipendente.nome + " numero " + dipendente.telefono)
                            pywhatkit.sendwhatmsg("+39" + dipendente.telefono, mex, ora, minuto)
                    QMessageBox.information(None, "RGest", str50)

    def prenotazioni(self):
        self.lpv.show()

    def dipendenti(self):
        self.ldv.show()

    def comanda(self):
        self.lcomandav_noDelivery.show()

    def costi_covid(self):
        self.ccv = costi_covid_view(self.lccc, self.lingua)
        self.ccv.show()

    def tasse(self):
        self.tv = tasse_view(self.ltc, self.lingua)
        self.tv.show()

    def costi(self):
        self.cv = costi_view(self.lingua)
        self.cv.show()

    def guadagni(self):
        self.gv = guadagni_view(self.lingua)
        self.gv.show()

    def dati_clienti(self):
        self.lclientiv = lista_clienti_view(self.lingua)
        self.lclientiv.show()

    def chiamate(self):
        self.ldeliveryv = lista_delivery_view(self.lingua)
        self.ldeliveryv.show()

    def comandaDelivery(self):
        self.lcomandav_Delivery.show()

    def ordine_materie(self):
        self.lordiniMPv = lista_ordiniMP_view(self.lingua)
        self.lordiniMPv.show()

    def consumo_materie(self):
        self.consumoMPv = consumoMP_view(self.lingua)
        self.consumoMPv.show()

    def magazzino_click(self):
        self.magazzinov = magazzino_view(self.lingua)
        self.magazzinov.show()

    def grafico(self):
        global str2__, str1__
        if self.lingua == "Inglese":
            str1__ = "No plates sold"
            str2__ = "Statistics plates sold"
        if self.lingua == "Italiano":
            str1__ = "Nessun piatto venduto"
            str2__ = "Statistiche piatti più venduti"

        self.lpiattic = lista_piatti_controller()
        valori = []
        nomi = []
        if not self.lpiattic.get_lista_stats():
            QMessageBox.warning(None, "RGest", str1__)
        else:
            for piatto in self.lpiattic.get_lista_piatti():
                valori.append(self.quanti((piatto.nome, piatto.prezzo)))
                nomi.append(piatto.nome)
            index = np.arange(len(nomi))
            p.title(str2__)
            p.bar(index, valori)
            p.xticks(index, nomi, size=8, rotation=90)
            p.show()

    def grafico_clienti(self):
        global __str2, __str1
        if self.lingua == "Inglese":
            __str1 = "No customers in the list"
            __str2 = "Most present customer statistics"
        if self.lingua == "Italiano":
            __str1 = "Nessun cliente nella lista"
            __str2 = "Statistiche clienti più presenti"

        self.lclientic = lista_clienti_controller()
        valori = []
        nomi = []
        if not self.lclientic.get_lista_clienti_noDoppi():
            QMessageBox.warning(None, "RGest", __str1)
        else:
            for cliente in self.lclientic.get_lista_clienti_noDoppi():
                valori.append(self.quanti_clienti((cliente.nome, cliente.telefono)))
                nomi.append(cliente.nome)
            index = np.arange(len(nomi))
            p.title(__str2)
            p.bar(index, valori)
            p.xticks(index, nomi, size=8, rotation=90)
            p.show()

    def quanti(self, portata):
        a = 0
        for p in self.lpiattic.get_lista_stats():
            if p == portata:
                a += 1
        return a

    def quanti_clienti(self, cliente):
        a = 0
        for p in self.lclientic.get_lista_clienti():
            if (p.nome, p.telefono) == cliente:
                a += 1
        return a
