# Programma, kas veic teksta aizšifrēšanu un atšifrēšanu latviešu alfabēta burtiem
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

teksts = input('Ievadiet teksta rindu --> ')
darb = input('Ievadiet vēlamo darbību (c - šifrēt, d - atšifrēt) --> ')
skaitlis = int(input('Ievadiet skaitļi šifrēšanai --> '))

#print(teksts)
#print(len(teksts))

teksts = teksts.upper()

simboli = []
for i in range(len(teksts)):
    if teksts[i] == ' ':
        simboli.append('_')
    else:
        simboli.append(teksts[i])

#print(simboli)

i = 0
soli = []
while len(soli) < len(simboli):
    for j in str(skaitlis):
        if len(soli) == len(simboli):
            break
        soli.append(int(j))

if darb == 'd':
    virz = -1
else:
    virz = 1
    
sifrs = []
for i in range(len(simboli)):
    simbols = simboli[i]
    v = alfabets.index(simbols)
    solis = soli[i] * virz
    jaun_v = v + solis
    
    if jaun_v < 0:
        jaun_v = len(alfabets)+1 + solis
        
    if jaun_v > len(alfabets)-1:
        jaun_v = jaun_v - len(alfabets)
        
    sifrs.append(alfabets[jaun_v])
    
rinda1 = ''
for i in range(len(simboli)):
    rinda1 += str(simboli[i])
    
rinda2 = ''
for i in range(len(soli)):
    rinda2 += str(soli[i])
    
rinda3 = ''
for i in range(len(sifrs)):
    rinda3 += str(sifrs[i])

print('')
print(rinda1)
print(rinda2)
print(rinda3)