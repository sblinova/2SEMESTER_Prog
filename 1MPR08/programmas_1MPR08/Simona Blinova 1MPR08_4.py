# Programma, kas nodrukā matricu ar tās diagonaļu elementu summu
# Programmas autors Simona Bļinova
# Versija 1.0

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


def summu_matrica(a):
    n = a.shape[0]
    b = numpy.zeros((n+1, n+1))
    for i in range(n):
        for j in range(n):
            b[i][j] = a[i][j]
    return b


def diagonalu_summas(a, b):
    n = a.shape[0]
    m = b.shape[0]
    k = 0
    while k < n:
        if k == 0:
            for i in range(n):
                b[m-1][m-1] += a[i][i]
        else:
            for i in range(n):
                if i+k < n:
                    b[m-1-k][m-1] += a[i][i+k]
                    b[m-1][m-1-k] += a[i+k][i]
                else:
                    break
        k += 1
    
    return b


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

print(' ')

summas = summu_matrica(matrica)

summas = diagonalu_summas(matrica, summas)

matricas_izvade(summas)
    
            