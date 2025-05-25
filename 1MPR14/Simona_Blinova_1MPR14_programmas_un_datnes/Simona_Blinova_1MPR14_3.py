# Programma, kas veic teksta šifrēšanu un atšifrēšanu ar Cēzara algoritmu
# Programmas autors Simona Bļinova
# Versija 1.0

teksts = input('Ievadiet tekstu --> ')
darb = input('Ko vēlaties darīt? (c - šifrēt, d - atšifrēt) --> ')
solis = int(input('Ievadiet šifrēšanas soli --> '))

teksts = teksts.upper()

simboli = []
for i in teksts:
    simboli.append(i)

#print(simboli)

if darb == 'c':
    solis = -solis

for i in range(len(simboli)):
    #print(i)
    burts = simboli[i]
    #print(burts)
    
    if 64 < ord(burts) < 91:
        jaun_burts = ord(burts) + solis
        if jaun_burts <= 64:
            plus_solis = 65 - jaun_burts
            jaun_burts = 91 - plus_solis
        
        if jaun_burts >= 91:
            plus_solis = jaun_burts - 90
            jaun_burts = 64 + plus_solis
            
        simboli[i] = chr(jaun_burts)
            
#print(simboli)

jaun_teksts = ''
for elem in simboli:
    jaun_teksts += elem
    
print(jaun_teksts)
        
    
        
    
