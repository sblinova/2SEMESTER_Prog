# Programma, kas parraksta informaciju parveidojot burtu par uppercase
# Programmas autors Simona Blinova
# Verisja 1.0

import os
import sys

# jāpievieno pareizas cēļš līdz datnei
datnes_cels1 = 'C:/Users/Simona/Desktop/lu/programmesana un datori I/2sem/1MPR14/Simona_Blinova_1MPR14_programmas_un_datnes/uzd1 test1.txt'
if not os.path.isfile(datnes_cels1):
    print(f'Kļuda: Datne "{datnes_cels1}" neeksistē.')
    sys.exit(1)
    
# jāpievieno pareizas cēļš līdz datnei
datnes_cels2 = 'C:/Users/Simona/Desktop/lu/programmesana un datori I/2sem/1MPR14/Simona_Blinova_1MPR14_programmas_un_datnes/uzd1 test2.txt'
if not os.path.isfile(datnes_cels2):
    print(f'Kļuda: Datne "{datnes_cels2}" neeksistē.')
    sys.exit(1)

with open('uzd1 test1.txt', 'w', encoding='utf-8') as datne:
    while True:
        rinda = input('Ievadiet teksta rindu --> ')
        datne.write(rinda + '\n')
        print('')
        
        paz = input('Vai vēlaties ievadīt vēl rindu? (n - nē) --> ')
        print('')
            
        if paz == 'n':
            break
            
    datne.close()
    
with open('uzd1 test1.txt', 'r', encoding='utf-8') as datne1, \
     open('uzd1 test2.txt', 'w', encoding='utf-8') as datne2:
    saturs = datne1.read()
    #print(saturs)
    
    for b in saturs:
        #print(b)
        try:
            b = b.upper()
            datne2.write(b)
        except:
            datne2.write(b)
    
    datne1.close()
    datne2.close()
    
            
    
