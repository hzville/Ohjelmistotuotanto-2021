class Summa:

    def __init__(self,sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.aseta_edellinen_tulos()
        self.sovelluslogiikka.tulos= self.sovelluslogiikka.tulos + int(self.syote())