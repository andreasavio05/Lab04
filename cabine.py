class Cabine:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo

    def __str__(self):
        return f'{self.codice} {self.letti} {self.ponte} {self.prezzo}'

    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(codice={self.codice}, letti={self.letti}, ponte={self.ponte},prezzo={self.prezzo})')