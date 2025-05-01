# Programma, kas izveido klasi Taisturis un izvada objekta perimetru un laukumu
# Programmas autors Simona Bļinova
# Versija 1.0

class Taisnsturis():
    '''
    Klase 'Taisnsturis' pārstāv vienkāršu taisnstūra modeli ar pamatinformāciju:
    garums, platums
    
    Šī klase nodrošina metodes laukuma, perimetra aprēķiniem un informācijas izvadei.
    
    Lauki:
        garums (int): Taisntūra garums
        platums (int): Taisnstūra platums
    
    Metodes:
        perimetrs()
        laukums()
        __str__()
    '''
    
    def __init__(self, garums, platums):
        '''
        Konstruktors (inicializators).
        Piešķir sākotnējās vērtības laukiem.
        
        Argumenti:
            garums (int): Taisntūra garums
            platums (int): Taisnstūra platums
        '''   
        
        self.garums = garums
        self.platums = platums
        
    def perimetrs(self):
        '''
        Metode.
        Aprēķina objekta perimetru.
        '''
        
        return f'Perimetrs: {(self.garums + self.platums) * 2}'
    
    def laukums(self):
        '''
        Metode.
        Aprēķina objekta laukumu.
        '''
        
        return f'Laukums: {self.garums * self.platums}'
    
    def __str__(self):
        '''
        Metode.
        Izvada informāciju par objektu.
        '''
        
        return f'Taisnstūris {self.garums} x {self.platums}'
    
    
def galvena_programma():
    x = int(input('Ievaidet taisnstūra garumu --> '))
    y = int(input('Ievaidet taisnstūra platumu --> '))
    z = Taisnsturis(x, y)
    print(z)
    print(z.perimetrs())
    print(z.laukums())


if __name__ == '__main__':
    galvena_programma()
    #mans_taisnsturis = Taisnsturis(4, 4)
    ##mans_taisnsturis2 = Taisnsturis(6, 2)
    
    #print(mans_taisnsturis)
    
    #print(mans_taisnsturis.perimetrs())
    #print(mans_taisnsturis.laukums())