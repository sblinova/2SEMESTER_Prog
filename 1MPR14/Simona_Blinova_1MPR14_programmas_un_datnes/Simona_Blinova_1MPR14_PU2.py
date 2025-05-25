# Programma, kas veic teksta šifrēšanu un atšifrēšanu ar Cēzara algoritmu.
# Programmas autors Simona Bļinova
# Versija 1.0

lat_burti = ['Ā', 'Č', 'Ē', 'Ģ', 'Ī', 'Ķ', 'Ļ', 'Ņ', 'Š', 'Ū', 'Ž']
alfabets = []

for i in range(65, 81):
    alfabets.append(chr(i))
    
for i in range(82, 87):
    alfabets.append(chr(i))
    
alfabets.append(chr(90))

i = 0
burts = alfabets[i]
while burts != 'Ž':
    match burts:
        case 'A':
            alfabets.insert(i+1, 'Ā')
        case 'C':
            alfabets.insert(i+1, 'Č')
        case 'E':
            alfabets.insert(i+1, 'Ē')
        case 'G':
            alfabets.insert(i+1, 'Ģ')
        case 'I':
            alfabets.insert(i+1, 'Ī')
        case 'K':
            alfabets.insert(i+1, 'Ķ')
        case 'L':
            alfabets.insert(i+1, 'Ļ')
        case 'N':
            alfabets.insert(i+1, 'Ņ')
        case 'S':
            alfabets.insert(i+1, 'Š')            
        case 'U':
            alfabets.insert(i+1, 'Ū')
        case 'Z':
            alfabets.insert(i+1, 'Ž')  
    i += 1
    burts = alfabets[i]

#print(alfabets)

teksts = input('Ievadiet tekstu --> ')
darb = input('Ko vēlaties darīt? (c - šifrēt, d - atšifrēt) --> ')
solis = int(input('Ievadiet šifrēšanas soli --> '))

teksts = teksts.upper()

simboli = []
for i in teksts:
    simboli.append(i)

if darb == 'c':
    solis = -solis

for i in range(len(simboli)):
    #print(i)
    burts = simboli[i]
    vieta = alfabets.index(burts)
    #print(vieta)
    
    if -1 < vieta < len(alfabets):
        jaun_vieta = vieta + solis
        #print(jaun_vieta)
        if jaun_vieta <= -1:
            jaun_vieta = len(alfabets) + jaun_vieta
            #print(jaun_vieta)
        
        if jaun_vieta >= len(alfabets):
            plus_solis = jaun_vieta - len(alfabets)
            #print(plus_solis)
            jaun_vieta = 0 + plus_solis
            
        simboli[i] = alfabets[jaun_vieta]
            
#print(simboli)

jaun_teksts = ''
for elem in simboli:
    jaun_teksts += elem
    
print(jaun_teksts)