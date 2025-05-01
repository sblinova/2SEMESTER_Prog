# Programma ar klasi Trijsturis, kas satur noteiktas metodes
# Programmas autors Simona Bļinova
# Versija 1.0

import math

class Trijsturis:
    '''
    Klase 'Trijsturis' pārstāv vienkāršu trijstūra modeli ar pamatinformāciju:
    mala1, mala2, mala3
    
    Šī klase nodrošina metodes laukuma, perimetra, apvilktas un ievilktas riņķa lījas radiusa aprēķiniem un trijstūra malu garumu izvadi.
    
    Lauki:
        mala1 (int): 1. trijstūra mala
        mala2 (int): 2. trijstūra mala
        mala3 (int): 3. trijstūra mala
    
    Metodes:
        perimetrs()
        laukums()
        ievilktas_rinka_linijas_radiuss()
        apvilktas_rinka_linijas_radiuss()
        __str__()
    '''
    
    def __init__(self, mala1, mala2, mala3):
        '''
        Konstruktors (inicializators).
        Piešķir sākotnējās vērtības laukiem.
        
        Argumenti:
            mala1 (int): 1. trijstūra mala
            mala2 (int): 2. trijstūra mala
            mala3 (int): 3. trijstūra mala
        '''   
        
        self.mala1 = mala1
        self.mala2 = mala2
        self.mala3 = mala3
        
    def perimetrs(self):
        '''
        Metode.
        Aprēķina objekta perimetru.
        '''
        
        return self.mala1 + self.mala2 + self.mala3
    
    def laukums(self):
        '''
        Metode.
        Aprēķina objekta laukumu.
        '''
        
        p = self.perimetrs()
        #print(p)
        pusp = p / 2
        return round(math.sqrt(pusp * (pusp - self.mala1) * (pusp - self.mala2) * (pusp - self.mala3)), 2)
    
    def ievilktas_rinka_linijas_radiuss(self):
        '''
        Metode.
        Aprēķina objekta ievilktas rinka linijas radiusu.
        '''        
        
        s = self.laukums()
        p = self.perimetrs()
        return round(2 * s / p, 2)
    
    def apvilktas_rinka_linijas_radiuss(self):
        '''
        Metode.
        Aprēķina objekta apvilktas rinka linijas radiusu.
        '''  
        
        s = self.laukums()
        return round(self.mala1 * self.mala2 * self.mala3 / 4 / s, 2)
    
    def __str__(self):
        '''
        Metode.
        Izvada visu sākotnējo informāciju par objektu.
        '''
        return f'Trijstūris {self.mala1}x{self.mala2}x{self.mala3}'
      
    
def galvena_programma():
    m1 = int(input('Ievaidet trijstūra 1. malu --> '))
    m2 = int(input('Ievaidet trijstūra 2. malu --> '))
    m3 = int(input('Ievadiet trijstūra 3. malu --> '))
    
    if m1+m2>m3 and m1+m3>m2 and m2+m3>m2:
        trijsturis = Trijsturis(m1, m2, m3)
        print(f'Perimetrs: {trijsturis.perimetrs()}')
        print(f'Laukums: {trijsturis.laukums()}')
        print(f'Ievilktas riņķa līnijas laukums: {trijsturis.ievilktas_rinka_linijas_radiuss()}')
        print(f'Apvilktas riņķa līnijas laukums: {trijsturis.apvilktas_rinka_linijas_radiuss()}') 
    else:
        print('Tadas malas trijstūrim nav iespējamas!')
        exit()
        
    
if __name__ == '__main__':
    galvena_programma()