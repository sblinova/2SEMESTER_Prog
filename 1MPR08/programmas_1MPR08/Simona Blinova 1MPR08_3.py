# Programma, kas pārbauda vai matrica veido maģisko kvadrātu
# Programmas autors Simona Bļinova
# Versija 1.0

import numpy

def parbaude(a):
    skaititajs = 1
    while skaititajs <= 3:
        try:
            a = int(a)
            if a < 1:
                raise Exception
            else:
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


def vai_magiskais(a):
    n = a.shape[0]
    summas = []
    
    # Horizontāles
    for i in range(n):
        s = 0
        for j in range(n):
            s += a[i][j]
        summas.append(s)
        
    # Vertikāles
    for i in range(n):
        s = 0
        for j in range(n):
            s += a[j][i]
        summas.append(s)
    
    # Galvenā diagonāle
    s = 0
    for i in range(n):
        s += a[i][i]
    summas.append(s)
    
    # Otrā diagonāle
    s = 0
    for i in range(n-1, -1, -1):
        s += a[i][i]
    summas.append(s)
    
    p = summas[0]
    for i in range(1, len(summas)):
        if p != summas[i]:
            break
    else:
        return True, p
    
    return False, p


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


n = int(input('Ievadiet matricas rindu un kolonnu skaitu --> '))

matrica = numpy.empty((n, n))

matrica = elementu_ievade(matrica)

paz, summa = vai_magiskais(matrica)
#print(paz, summa)

print(' ')

if paz == False:
    print('Matrica neveido maģisko kvadrātu.')
    matricas_izvade(matrica)
else:
    print('Matrica veido maģisko kvadrātu.')
    jauna_matrica = numpy.empty((n+2, n+2))
    
    for i in range(n+2):
        for j in range(n+2):
            if i == 0 or i == n+1 or j == 0 or j == n+1:
                jauna_matrica[i][j] = summa
            else:
                jauna_matrica[i][j] = matrica[i-1][j-1]
                
    matricas_izvade(jauna_matrica)