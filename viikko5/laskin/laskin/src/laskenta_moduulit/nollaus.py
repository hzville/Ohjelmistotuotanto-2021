class Nollaus:

    def __init__(self,sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.aseta_edellinen_tulos()
        self.sovelluslogiikka.tulos= 0