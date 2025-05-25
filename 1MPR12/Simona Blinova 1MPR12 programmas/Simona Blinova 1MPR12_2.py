# Programma, kas nosaka dažādu figūru apkārtmēru un laukumu
# Programmas autors Simona Bļinova
# Versija 1.0

import math

class Figura:
    def __init__(self):
        self._pi = 3.14
        
    def perimetrs(self):
        pass    
    
    def laukums(self):
        pass
    
    
class Taisnsturis(Figura):
    def __init__(self, garums, platums):
        self.garums = garums
        self.platums = platums
        
    def perimetrs(self):
        return (self.garums + self.platums) * 2
    
    def laukums(self):
        return self.garums * self.platums
    
    
class Rinkis(Figura):
    def __init__(self, radiuss):
        super().__init__()
        self.radiuss = radiuss
        
    def perimetrs(self):
        return 2 * self._pi * self.radiuss
    
    def laukums(self):
        return self._pi * self.radiuss ** 2
    
    
class Trijsturis(Figura):
    def __init__(self, mala1, mala2, mala3):
        self.mala1 = mala1
        self.mala2 = mala2
        self.mala3 = mala3
        
    def perimetrs(self):
        return self.mala1 + self.mala2 + self.mala3
    
    def laukums(self):
        pusp = self.perimetrs() / 2
        return math.sqrt(pusp * (pusp-self.mala1) * (pusp - self.mala2) * (pusp - self.mala3))
    
    
def izdrukat_informaciju(figura):
    print(f'Perimetrs: {figura.perimetrs()}')
    print(f'Laukums: {figura.laukums()}')
    

def galvena_programma():
    print('Iespējamas darbības:')
    print('  --- izveidot taisnstūri (t)')
    print('  --- izveidot riņķi (r)')
    print('  --- izveidot trijstūri (tr)')
    print('  --- beigt darbu (b)')
    
    while True:
        print(' ')
        darb = input('Ko vēlaties darīt? (t, r, tr, b) --> ')
        print(' ')
        
        match darb:
            case 't':
                g = int(input('Ievadiet taisnstūra garumu --> '))
                p = int(input('Ievadiet taisnstūra platumu --> '))
                
                if g < 1 or p < 1:
                    print('Tāda mala nevar būt!')
                else:
                    f = Taisnsturis(g, p)
                    izdrukat_informaciju(f)
                    
            case 'r':
                r = int(input('Ievadiet riņķa līnijas radiusu --> '))
                
                if r < 1:
                    print('Tāds radiuss nevar būt!')
                else:
                    f = Rinkis(r)
                    izdrukat_informaciju(f)
                    
            case 'tr':
                m1 = int(input('Ievadiet 1. malas garumu --> '))
                m2 = int(input('Ievadiet 2. malas garumu --> '))
                m3 = int(input('Ievadiet 3. malas garumu --> '))
                
                if m1 < 1 or m2 < 1 or m3 < 1:
                    print('Tādas malas nevar būt!')
                elif m1 + m2 > m3 and m1 + m3 > m2 and m2 + m3 > m1:
                    f = Trijsturis(m1, m2, m3)
                    izdrukat_informaciju(f)
                else:
                    print('Tāds trijstūris nevar būt!')
                    
            case 'b':
                print('Programma beidz darbību.')
                exit()
            
            case _:
                print('Tādas darbības nav!')
                
if __name__ == '__main__':
    galvena_programma()
                
    