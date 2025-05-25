# Programma, kas realizē veikala simulāciju
# Programmas autors Simona Bļinova
# Versija 1.0

class Prece:
    def __init__(self, artikuls, nosaukums, daudzums, cena):
        self.artikuls = artikuls
        self.nosaukums = nosaukums
        self.daudzums = daudzums
        self.cena = cena
        
    def __str__(self):
        return f'{self.nosaukums} (Artikuls: {self.artikuls}) - {self.daudzums} gab., {self.cena:.2f} EUR'
    
class Veikals:
    def __init__(self):
        self.krajumi = {} # key: preces nosaukums, vertiba: prece objekts
        
    def pievienot_preci(self, prece):
        if prece.nosaukums in self.krajumi:
            self.krajumi[prece.nosaukums].daudzums += prece.daudzums
        else:
            self.krajumi[prece.nosaukums] = prece
            
    def paradit_preces(self):
        print('Pieejamas preces veikalā:')
        for prece in self.krajumi:
            print(prece)
            
    def ir_prece(self, nosaukums, daudzums):
        return nosaukums in self.krajumi and self.krajumi[nosaukums].daudzums >= daudzums
    
    def pardod_preci(self, nosaukums, daudzums):
        if self.ir_prece(nosaukums, daudzums):
            prece = self.krajumi[nosaukums]
            prece.daudzums -= daudzums
            return Prece(prece.artikuls, nosaukums, daudzums, prece.cena)
        else:
            print(f'Nav pietiekami daudz preces: {nosaukums}')
            return None
        
class Grozs:
    def __init__(self):
        self.pirkumi = [] 
        
    def pievienot_pirkumu(self, prece):
        self.pirkumi.append(prece)
        
    def izdrukat_cekus(self):
        print('Pirkuma čeks:')
        kopa = 0
        for prece in self.pirkumi:
            summa = prece.daudzums * prece.cena
            print(f'{prece.nosaukums} x {prece.daudzums} = {summa:.2f} EUR')
            kopa += summa
        print(f'Kopa jamaksa: {kopa:.2f} EUR')
        
def galvena_programma():
    veikals = Veikals()
    
    print('~~~ Preču piegāde veikalām ~~~')
    while True:
        artikuls = input('\nIevadiet artikulu --> ')
        nosaukums = input('Ievadiet preces nosaukumu --> ')
        daudzums = int(input('Ievadiet daudzumu --> '))
        cena = float(input('Ievadiet preces cenu (EUR) --> '))
        veikals.pievienot_preci(Prece(artikuls, nosaukums, daudzums, cena))
        
        paz = input('\nVai pievienot vēl preces? (j/n)')
        if paz == 'n':
            break
    
    print(' ')
    veikals.paradit_preces()
    
    print('\n~~~ Iepirkšanas ~~~')
    grozs = Grozs()
    
    while True:
        nosaukums = input('\nIevadiet preces nosaukumu --> ')
        daudzums = int(input('Ievadiet daudzumu --> '))
        if veikals.ir_prece(nosaukums, daudzums):
            prece = veikals.pardod_preci(nosaukums, daudzums)
            grozs.pievienot_pirkumu(prece)
        else:
            print('Nav pieejams!')
            
        paz = input('\n Vai pievienot vēl preces? (j/n)')
        if paz == 'n':
            break        
    
    print('\n~~~ Grozs ~~~')
    print(' ')
    grozs.izdrukat_cekus()
    
if __name__ == '__main__':
    galvena_programma()