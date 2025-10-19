from cabine import Cabine

class Animali(Cabine):
    def __init__(self, codice, letti, ponte, prezzo, max_animali):
        super().__init__(codice, letti, ponte, prezzo)
        self.max_animali = int(max_animali)

    def prezzo_finale(self):
        return self.prezzo_base * (1 + 0.10 * self.max_animali)

    def __str__(self):
        stato_extra = f'Max animali: {self.max_animali}'
        return f'{super().__str__()}, - {stato_extra}'

    def __repr__(self):
        return f'{super().__repr__()}, max_animali={self.max_animali}'


