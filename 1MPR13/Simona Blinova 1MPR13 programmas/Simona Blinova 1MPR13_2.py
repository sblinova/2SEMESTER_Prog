# Programma, kas realizē darbības ar kompleksiem skaitļiem
# Programmas autors Simona Bļinova
# Versija 2.0

import math

class Kompleksais_skaitlis:
    def __init__(self, a, b):
        self.z = (a, b)
        
    def __str__(self):
        if self.z[0] == 0 and self.z[1] == 0:
            return '0'
        elif self.z[0] == 0:
            return f'{self.z[1]}i'
        elif self.z[1] == 0:
            return f'{self.z[0]}'
        elif self.z[1] < 0:
            return f'{self.z[0]} - {abs(self.z[1])}i'
        else:
            return f'{self.z[0]} + {self.z[1]}i'
        
        
class Darbibas:
    def __init__(self, sk1, sk2):
        self.darb = {}
        self.darb['sk1'] = sk1
        self.darb['sk2'] = sk2
        
    def saistitais(self):
        self.darb['saist1'] = Kompleksais_skaitlis(self.darb['sk1'].z[0], -self.darb['sk1'].z[1])
        self.darb['saist2'] = Kompleksais_skaitlis(self.darb['sk2'].z[0], -self.darb['sk2'].z[1])
        
    def modulis(self):
        self.darb['modulis1'] = str(math.sqrt(self.darb['sk1'].z[0]**2 + self.darb['sk1'].z[1]**2))
        self.darb['modulis2'] = str(math.sqrt(self.darb['sk2'].z[0]**2 + self.darb['sk2'].z[1]**2))
        
    def summa(self):
        a = self.darb['sk1'].z[0] + self.darb['sk2'].z[0]
        b = self.darb['sk1'].z[1] + self.darb['sk2'].z[1]
        self.darb['summa'] = Kompleksais_skaitlis(a, b)
        
    def reizinajums(self):
        a = self.darb['sk1'].z[0] * self.darb['sk2'].z[0] - self.darb['sk1'].z[1] * self.darb['sk2'].z[1]
        b = self.darb['sk1'].z[0] * self.darb['sk2'].z[1] + self.darb['sk2'].z[0] * self.darb['sk1'].z[1]
        self.darb['reizinajums'] = Kompleksais_skaitlis(a, b)
        
    def dalijums(self):
        if self.darb['sk2'].z[0] != 0 and self.darb['sk2'].z[1] != 0:
            saucejs = self.darb['sk2'].z[0] ** 2 + self.darb['sk2'].z[1] ** 2
            a_skait = self.darb['sk1'].z[0] * self.darb['sk2'].z[0] + self.darb['sk1'].z[1] * self.darb['sk2'].z[1]
            b_skait = self.darb['sk2'].z[0] * self.darb['sk1'].z[1] - self.darb['sk1'].z[0] * self.darb['sk2'].z[1]
            self.darb['dalijums'] = Kompleksais_skaitlis(a_skait/saucejs, b_skait/saucejs)
        else:
            self.darb['dalijums'] = '---'
        
def galvena_programma():
    a1 = float(input('Ievadiet reālo koeficientu 1. skaitlim --> '))
    b1 = float(input('Ievadiet imaginaro koeficientu 1. skaitlim --> '))
    skaitlis1 = Kompleksais_skaitlis(a1, b1)
    
    a2 = float(input('Ievadiet reālo koeficientu 2. skaitlim --> '))
    b2 = float(input('Ievadiet imaginaro koeficientu 2. skaitlim --> '))
    skaitlis2 = Kompleksais_skaitlis(a2, b2)
    
    print('')
        
    darbibas = Darbibas(skaitlis1, skaitlis2)
    
    darbibas.saistitais()
    darbibas.modulis()
    darbibas.summa()
    darbibas.reizinajums()
    darbibas.dalijums()
    
    vertibas = []
    for vertiba in darbibas.darb.values():
        vertibas.append(vertiba)
        
    print('Pirmais skaitlis:', vertibas[0])
    print('Otrais skaitlis:', vertibas[1])
    print('Pirmā skaitļa saistītais:', vertibas[2])
    print('Otrā skaitļa saistītais:', vertibas[3])
    print('Pirmā skaitļa modulis:', vertibas[4])
    print('Otrā skaitļa modulis:', vertibas[5])
    print('Skaitļu summa:', vertibas[6])
    print('Skaitļu reizinājums:', vertibas[7])
    print('Skaitļu dalījums:', vertibas[8])
        
if __name__ == '__main__':
    galvena_programma()