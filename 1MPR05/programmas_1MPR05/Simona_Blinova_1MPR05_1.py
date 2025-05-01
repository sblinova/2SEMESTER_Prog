# Programma, kas izpilda masīva kārtošanu dilstoša secībā 5 veidos
# Programmas autors Simona Bļinova
# Versija 1.4

import funkcijas
import random
import copy
import math

''' Funkciju bloks '''

def aizpildit_masivu(a, elementu_skaits):
    for i in range(elementu_skaits, 2, -1):
        b = random.randint(1, i-1)
        c = a[i]
        a[i] = a[b]
        a[b] = c

    return a            


def naiva_kartosana(a):
    garums = len(a)
    skaititajs = 0

    for i in range(1, garums-1):
        maksimala_vertiba = a[i]
        max_vertibas_indekss = i

        for j in range(i+1, garums):
            skaititajs += 1
            if maksimala_vertiba < a[j]:
                maksimala_vertiba = a[j]
                max_vertibas_indekss = j

        a[max_vertibas_indekss] = a[i]
        a[i] = maksimala_vertiba

    a[0] = skaititajs

    return a


def bubble_metode(a):
    garums = len(a)
    skaititajs = 0

    atkartojumi = garums - 1
    pazime = True
    while pazime:
        pazime = False

        for j in range(1, atkartojumi):
            skaititajs += 1
            if a[j] < a[j+1]:
                pazime = True
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b

        atkartojumi -= 1

    a[0] = skaititajs

    return a


def atspoles_metode(a):
    garums = len(a)
    skaititajs = 0

    for i in range(2, garums):
        skaititajs += 1
        if a[i-1] < a[i]:
            for j in range(i, 1, -1):
                skaititajs += 1
                if a[j-1] < a[j]:
                    b = a[j]
                    a[j] = a[j-1]
                    a[j-1] = b
                else:
                    break
                
    a[0] = skaititajs
                
    return a


def ievietosanas_metode(a):
    garums = len(a)
    skaititajs = 0

    for i in range(2, garums):
        skaititajs += 1
        x = a[i]
        j = i
        while j > 1 and a[j-1] < x:
            skaititajs += 1
            a[j] = a[j-1]
            j -= 1
        a[j] = x
        
    a[0] = skaititajs

    return a


def shell_metode(a):
    garums = len(a)
    skaititajs = 0
    solis = (3**math.floor(math.log(2*n+1, 3))-1)//2

    while solis >= 1:
        for i in range(1, solis+1):
            for j in range(solis+i, garums, solis):
                skaititajs += 1
                
                if a[j-solis] < a[j]:
                    b = a[j]
                    k = j

                    while a[k-solis] < b:
                        skaititajs += 1
                        a[k] = a[k-solis]
                        k -= solis
                        if k == i:
                            break
                    
                    a[k] = b
                  
        solis = (solis - 1) // 3

    a[0] = skaititajs

    return a


def izvade(a):
    garums = len(a)
    virkne = ''

    for i in range(1, garums):
        if i == garums - 1:
            virkne += str(a[i])
        else:
            virkne += str(a[i]) + ', '

    return f'{a[0]} salīdzināšanas - {virkne}'


''' Masīva izveides un aizpildes bloks '''

n = input('Ievadiet masīva izmēru --> ')
n = funkcijas.naturals_skaitlis(n)

masivs = funkcijas.masiva_izveide(n+1)

masivs = aizpildit_masivu(masivs, n)
print(masivs)

'''Masīva kopijas kārtošana piecos veidos'''

masivs_naiva = naiva_kartosana(copy.deepcopy(masivs))
# print(masivs_naiva)

masivs_bubble = bubble_metode(copy.deepcopy(masivs))
# print(masivs_bubble)

masivs_atspole = atspoles_metode(copy.deepcopy(masivs))
# print(masivs_atspole)

masivs_ievietosana = ievietosanas_metode(copy.deepcopy(masivs))
# print(masivs_ievietosana)

masivs_shell = shell_metode(copy.deepcopy(masivs))
# print(masivs_shell)

''' Rezultātu izvade '''

print(f'Naivā kārtošanas metode: {izvade(masivs_naiva)}')
print(f'Burbuļa kārtošanas metode: {izvade(masivs_bubble)}')
print(f'Atspoles kārtošanas metode: {izvade(masivs_atspole)}')
print(f'Ievietošanas kārtošanas metode: {izvade(masivs_ievietosana)}')
print(f'Šella kārtošanas metode: {izvade(masivs_shell)}')