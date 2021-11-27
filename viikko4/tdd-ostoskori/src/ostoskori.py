from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.lista_ostoksista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        to_return = 0
        print(self.lista_ostoksista)
        for ostos in self.lista_ostoksista:
            to_return += ostos.lukumaara()
        return to_return
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        print("lisaa tuote")
        if len(self.lista_ostoksista) < 1:
            self.lista_ostoksista.append(Ostos(lisattava))
        else:
            for ostos in self.lista_ostoksista:
                if ostos.tuotteen_nimi == lisattava.nimi:
                    print("found already in ostokori")
                    ostos.muuta_lukumaaraa(1)
                else:
                    print("append to ostoskori")
                    self.lista_ostoksista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
