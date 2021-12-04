class Kumoa:

    def __init__(self,sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.edellinen_tulos)