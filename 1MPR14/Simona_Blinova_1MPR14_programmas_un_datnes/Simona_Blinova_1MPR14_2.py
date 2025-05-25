# Programma, kas teksta datnē saņem katra burta biežumu
# Programmas autors Simona Bļinova
# Versija 1.0

import os
import sys

# jāpievieno pareizas cēļš līdz datnei
datnes_cels = 'C:/Users/Simona/Desktop/lu/programmesana un datori I/2sem/1MPR14/Simona_Blinova_1MPR14_programmas_un_datnes/uzd2 test1.txt' 
if not os.path.isfile(datnes_cels):
    print(f'Kļuda: Datne "{datnes_cels}" neeksistē.')
    sys.exit(1)

with open('uzd2 test1.txt', 'w', encoding='utf-8') as datne:
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

with open('uzd2 test1.txt', 'r', encoding='utf-8') as datne:
    simbols = datne.read(1)
    while simbols != '':
        while simbols != '\n' and simbols != '':
            simbols = simbols.upper()
            if 64 < ord(simbols) < 91:
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

garums = len(skaiti)
atkartojumi = garums - 1
pazime = True

while pazime:
    pazime = False
    for j in range(0, atkartojumi):
        if skaiti[j] < skaiti[j+1]:
            pazime = True
            
            b = skaiti[j]
            skaiti[j] = skaiti[j+1]
            skaiti[j+1] = b
            
            b1 = burti[j]
            burti[j] = burti[j+1]
            burti[j+1] = b1
            
            atkartojumi -= 1
            
#print(burti)
#print(skaiti)

for i in range(len(burti)):
    print(burti[i], '->', skaiti[i])



