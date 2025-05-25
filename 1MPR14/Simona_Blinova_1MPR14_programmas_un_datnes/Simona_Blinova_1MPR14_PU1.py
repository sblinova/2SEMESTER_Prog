# Programma, kas teksta datnē saņem katra latviešu burta biežumu
# Programmas autors Simona Bļinova
# Versija 1.0

import os
import sys

def ievietosanas_metode(a, b):
    garums = len(a)

    for i in range(1, garums):
        x = a[i]
        xb = b[i]
        j = i
        while j > 0 and a[j-1] < x:
            a[j] = a[j-1]
            b[j] = b[j-1]
            j -= 1
        a[j] = x
        b[j] = xb

    return a, b

datnes_cels = 'C:/Users/Simona/Desktop/lu/programmesana un datori I/2sem/1MPR14/Simona_Blinova_1MPR14_programmas_un_datnes/PU1 test.txt'
if not os.path.isfile(datnes_cels):
    print(f'Kļuda: Datne "{datnes_cels}" neeksistē.')
    sys.exit(1)

with open('PU1 test.txt', 'w', encoding='utf-8') as datne:
    while True:
        rinda = input('Ievadiet teksta rindu --> ')
        datne.write(rinda + '\n')
        print('')
        
        paz = input('Vai vēlaties ievadīt vēl rindu? (n - nē) --> ')
        print('')
        
        if paz == 'n':
            break
        
    datne.close()
    
vardnica = {}
lat_burti = [256, 268, 274, 286, 298, 310, 315, 325, 352, 362, 381]

with open('PU1 test.txt', 'r', encoding='utf-8') as datne:
    simbols = datne.read(1)
    while simbols != '':
        while simbols != '\n' and simbols != '':
            simbols = simbols.upper()
            if 64 < ord(simbols) < 81 or 81 < ord(simbols) < 87 or ord(simbols) == 90 or ord(simbols) in lat_burti:
                if simbols in vardnica:
                    vardnica[simbols] += 1
                else:
                    vardnica[simbols] = 1
            simbols = datne.read(1)
        if simbols == '\n':
            simbols = datne.read(1)

#print(vardnica)
burti = list(vardnica.keys())
#print(burti)
skaiti = list(vardnica.values())
#print(skaiti)
            
#print(burti)
#print(skaiti)

skaiti, burti = ievietosanas_metode(skaiti, burti)

#print(burti)
#print(skaiti)

for i in range(len(burti)):
    print(burti[i], '->', skaiti[i])