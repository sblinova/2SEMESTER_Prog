# Programma, kas veic matriču atbilstošo elementu reizināšānu un matricu reizināšanu, ja tas ir iespējams
# Programmas autors Simona Bļinova
# Versija 1.1

import numpy

def parbaude(a):
    skaititajs = 1
    while skaititajs < 3:
        try:
            a = int(a)
            return int(a)
        except:
            skaititajs += 1
            a = input('Ievadiet elementu vēlreiz --> ')
    else:
        print('Programma beidz darbību!')
        exit()
    

def elementu_ievade(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            b = input('Ievadiet matricas elementu a('+str(i+1)+','+str(j+1)+') --> ')
            b = parbaude(b)
            a[i][j] = b
    return a


def elementu_reizinajums(a, b):
    n1 = a.shape[0]
    m1 = a.shape[1]
    n2 = b.shape[0]
    m2 = b.shape[1]
    if n1 == n2 and m1 == m2:
        c = numpy.empty((n1, m1))
        for i in range(n1):
            for j in range(m1):
                c[i][j] = a[i][j] * b[i][j]
    else:
        c = numpy.zeros((1, 1))
        c[0][0] = 0.1
        
    return c
    

def matricu_reizinajums(a, b):
    n1 = a.shape[0]
    m1 = a.shape[1]
    n2 = b.shape[0]
    m2 = b.shape[1]
    if m1 == n2:
        c = numpy.zeros((n1, m2))
        for i in range(n1):
            for j in range(m2):
                for k in range(m1):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
    else:
        c = numpy.empty((1, 1))
        c[0][0] = 0.1
        
    return c
    
    
def matricas_min(a):
    min_elem = a[0][0]
    rinda = 0
    kolonna = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if min_elem > a[i][j]:
                min_elem = a[i][j]
                rinda = i
                kolonna = j
    return min_elem, rinda, kolonna


def matricas_max(a):
    max_elem = a[0][0]
    rinda = 0
    kolonna = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if max_elem < a[i][j]:
                max_elem = a[i][j]
                rinda = i
                kolonna = j
    return max_elem, rinda, kolonna
    

def matricas_izvade(a):
    
    minimums, min_rinda, min_kolonna = matricas_min(a)
    maksimums, max_rinda, max_kolonna = matricas_max(a)
    
    if len(str(minimums)) > len(str(maksimums)):
        garums = len(str(minimums))
    else:
        garums = len(str(maksimums))    
        
    for i in range(len(a)):
        virkne = ''
        for j in range(len(a[i])):
            skaits = garums - len(str(a[i][j]))
            virkne = virkne + ' '*skaits
            virkne = virkne + '{:.0f}'.format(a[i][j])
            if j == len(a[i]) - 1:
                print(virkne)
            else:
                virkne = virkne + ' '


rindas1 = int(input('Ievadiet 1.matricas rindu skaitu --> '))
kolonnas1 = int(input('Ievadiet 1.matricas kolonnu skaitu --> '))

matrica1 = numpy.empty((rindas1, kolonnas1))
matrica1 = elementu_ievade(matrica1)

rindas2 = int(input('Ievadiet 2.matricas rindu skaitu --> '))
kolonnas2 = int(input('Ievadiet 2.matricas kolonnu skaitu --> '))

matrica2 = numpy.empty((rindas2, kolonnas2))
matrica2 = elementu_ievade(matrica2)

print(' ')
matricas_izvade(matrica1)

print(' ')
matricas_izvade(matrica2)

print(' ')

print('Matricas atbilstošo elementu reizinājums: ')
rez1_matrica = elementu_reizinajums(matrica1, matrica2)
if rez1_matrica[0][0] == 0.1:
    print('Nevar sareizināt atbilstošos elementus dažāda izmēra matricām.')
else:
    matricas_izvade(rez1_matrica)
    
print(' ')

print('Matricu reizinājums: ')
rez2_matrica = matricu_reizinajums(matrica1, matrica2)
if rez2_matrica[0][0] == 0.1:
    print('Nevar sareizināt matricas ar šadiem izmēriem.')
else:
    matricas_izvade(rez2_matrica)


