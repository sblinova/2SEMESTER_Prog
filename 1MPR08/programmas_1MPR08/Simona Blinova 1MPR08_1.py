# Programma, kas izveido masīvu, atrod mazāko un lielāko vērtību un nodrukā masīvu tabulas veidā
# Programmas autors Simona Bļinova
# Versija 1.2

import numpy

def parbaude(a):
    skaititajs = 1
    while skaititajs <= 3:
        try:
            a = int(a)
            if a > 9999 or a < -999:
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


def matricas_izvade(a, g):
    for i in range(len(a)):
        virkne = ''
        for j in range(len(a[i])):
            skaits = g - len(str(a[i][j]))
            virkne = virkne + ' '*skaits
            virkne = virkne + '{:.0f}'.format(a[i][j])
            if j == len(a[i]) - 1:
                print(virkne)
            else:
                virkne = virkne + ' '
                

rindas = int(input('Ievadiet matricas rindu skaitu --> '))
kolonnas = int(input('Ievadiet matricas kolonnu skaitu --> '))

matrica = numpy.empty((rindas, kolonnas))

matrica = elementu_ievade(matrica)
#print(masivs)

minimums, min_rinda, min_kolonna = matricas_min(matrica)
maksimums, max_rinda, max_kolonna = matricas_max(matrica)

if len(str(minimums)) > len(str(maksimums)):
    garums = len(str(minimums))
else:
    garums = len(str(maksimums))

print(' ')
matricas_izvade(matrica, garums)
print(' ')
print(f'Mazākais elements ir {int(minimums)}, un tas atrodas {min_rinda+1}.rindas un {min_kolonna+1}.kolonnas krustpunktā')
print(f'Lielākais elements ir {int(maksimums)}, un tas atrodas {max_rinda+1}.rindas un {max_kolonna+1}.kolonnas krustpunktā')