from cabine import Cabine

class Animali(Cabine):
    def __init__(self, codice, letti, ponte, prezzo, max_animali):
        super().__init__(codice, letti, ponte, prezzo)
        self.max_animali = int(max_animali)

    def __str__(self):
        return f'{super().__str__()}, {self.max_animali}'

    def __repr__(self):
        return f'{super().__repr__()}, max_animali={self.max_animali}'

    def incremento_prezzo(self):
        self.prezzo = self.prezzo * (1 + 0.10 * self.max_animali)
