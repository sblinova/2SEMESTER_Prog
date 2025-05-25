# Programma, kas aprēķina n-stūra laukumu
# Programmas autors Simona Bļinova
# Versija 1.0

class Virsotne:
    def __init__(self, x, y):
        self.koordinatas = (x, y)
        
class Nsturis:
    def __init__(self, virsotnes):
        self.virsotnes = virsotnes
        
    def pievienot_virsotni(self, x, y):
        self.virsotnes.append(Virsotne(x, y))
        
    def laukums(self):
        if len(self.virsotnes) < 3:
            return 'Virsotņu skaits nav pietiekams laukuma aprēķinam.'
        else:
            summa = 0
            for i in range(len(self.virsotnes)-1):
                #print(self.virsotnes[i].koordinatas[0], self.virsotnes[i+1].koordinatas[0])
                s = (self.virsotnes[i].koordinatas[0] + self.virsotnes[i+1].koordinatas[0]) * (self.virsotnes[i].koordinatas[1] - self.virsotnes[i+1].koordinatas[1])
                summa += s
            abs_summa = abs(summa)
            return abs_summa / 2
        
def galvena_programma():
    print('N-stūra virsotņu ievade')
    print('')
    
    v = []
    nsturis = Nsturis(v)
    
    while True:
        koord_x = float(input('Ievadiet x koordinātu --> '))
        koord_y = float(input('Ievadiet y koordinātu --> '))
        nsturis.pievienot_virsotni(koord_x, koord_y)
        print('')
        
        turp = input('Vēlaties turpināt ievadi? (t - turpināt, p - pabeigt) --> ')
        print('')
        
        if turp == 'p':
            break
        
    print('')
    print('Laukuma aprēķins')
    print('')
    
    print(f'Laukums: {nsturis.laukums()}')
        
if __name__ == '__main__':
    galvena_programma()