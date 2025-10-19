from cabine import Cabine

class Deluxe(Cabine):
    def __init__(self, codice, letti, ponte, prezzo, tipologia):
        super().__init__(codice, letti, ponte, prezzo)
        self.tipologia = tipologia

    def prezzo_finale(self):
        return self.prezzo_base * 1.20

    def __str__(self):
        stato_extra = f'Tipologia: {self.tipologia}'
        return f'{super().__str__()}, - {stato_extra}'

    def __repr__(self):
        return f'{super().__repr__()}, tipologia={self.tipologia}'