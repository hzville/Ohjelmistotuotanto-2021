# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote

ostoskori = Ostoskori()
maito = Tuote("Maito", 3)
leipa = Tuote("Leipa", 2)
ostoskori.lisaa_tuote(maito)
ostoskori.lisaa_tuote(maito)
