# Programma, kas realizē Latloto 5 no 35 izlozi
# Programmas autors Simona Bļinova
# Versija 1.1

import random

def izloze():
    l = set()
    for i in range(5):
        while True:
            x = random.randint(1, 35)
            if not x in l:
                l.add(x)
                break
    return l


def bilete():
    b = set()
    for i in range(5):
        while True:
            x = int(input(f'Ievadiet {i+1} skaitli --> '))
            if not x < 1 and not x > 35:
                if not x in b:
                    b.add(x)
                    break
    return b
            

b = bilete()    
l = izloze()
#print(b, l)

skel = b & l
#print(skel)

match len(skel):
    case 3:
        laimests = 'Jūs atminējat 3 skaitļus, jūs saņēmāt MAZO LAIMESTU!'
    case 4:
        laimests = 'Jūs atminējat 4 skaitļus, jūs saņēmāt VIDĒJO LAIMESTU!'
    case 5:
        laimests = 'Jūs atminējat 5 skaitļus, jūs saņēmāt LIELO LAIMESTU!'
    case _:
        laimests = 'Jums NAV LAIMESTA!'

print(' ')
print(f'Izlozētie skaitļi: ', l)
print(f'Jūsu skaitļi: ', b)
print(laimests)