from passeggeri import Passeggeri
from cabine import Cabine
from cabine_animali import Animali
from cabine_deluxe import Deluxe
from csv import reader
from operator import attrgetter

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.passeggeri = []
        self.cabine = []
        self.animali = []
        self.deluxe = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, 'r', encoding='UTF-8') as file:
                csv_reader = reader(file)
                for line in csv_reader:
                    if len(line) == 3:
                        codice = line[0]
                        nome = line[1]
                        cognome = line[2]
                        passeggero = Passeggeri(codice, nome, cognome)
                        self.passeggeri.append(passeggero)
                    elif len(line) == 4:
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        cabina = Cabine(codice, letti, ponte, prezzo)
                        self.cabine.append(cabina)
                    elif len(line) == 5 and line[-1] == int:
                        codice = line[0]
                        letti = line[1]
                        ponte = line[2]
                        prezzo = line[3]
                        extra = line[4]
                        try:
                            max_animali = int(extra)
                            cabina = Animali(codice, letti, ponte, prezzo, max_animali)
                        except ValueError:
                            tipologia = extra
                            cabina = Deluxe(codice, letti, ponte, prezzo, tipologia)
                        self.cabine.append(cabina)
        except FileNotFoundError:
            raise FileNotFoundError('File non trovato')


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        cabina = None
        for c in self.cabine:
            if c.codice == codice_cabina:
                cabina = c
                break
        if cabina is None:
            raise Exception('Cabina non trovata')

        passeggero = None
        for p in self.passeggeri:
            if p.codice == codice_passeggero:
                passeggero = p
                break
        if passeggero is None:
            raise Exception('Passeggero non trovato')

        if not cabina.disponibile:
            raise Exception('Cabina non disponibile')
        if passeggero.cabina is not None:
            raise Exception('Passeggero già assegnato a una cabina')

        cabina.disponibile = False
        passeggero.assegna_cabina(cabina)

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabine, key=attrgetter('prezzo_base'))


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.passeggeri:
            print(p)

