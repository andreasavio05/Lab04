from cabine import Cabine

class Deluxe(Cabine):
    def __init__(self, codice, letti, ponte, prezzo, tipologia):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.tipologia = tipologia

    def __str__(self):
        return f'{super().__str__()}, {self.tipologia}'

    def __repr__(self):
        return f'{super().__repr__()}, tipologia={self.tipologia}'

    def incremento_prezzo(self):
        self.prezzo = self.prezzo * 1.20