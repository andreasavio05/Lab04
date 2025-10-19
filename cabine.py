class Cabine:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = int(letti)
        self.ponte = int(ponte)
        self.prezzo_base = float(prezzo)
        self.disponibile = True

    def prezzo_finale(self):
        return self.prezzo_base

    def __str__(self):
        if self.disponibile:
            stato = 'Disponibile'
        else:
            stato = 'Occupata'
        return f'{self.codice}: Standard | {self.letti} letti - Ponte {self.ponte} - Prezzo {self.prezzo_finale()}$ - {stato}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(codice={self.codice}, letti={self.letti}, ponte={self.ponte},prezzo={self.prezzo_base})')

    def __lt__(self, other):
        return self.prezzo_finale() < other.prezzo_finale()