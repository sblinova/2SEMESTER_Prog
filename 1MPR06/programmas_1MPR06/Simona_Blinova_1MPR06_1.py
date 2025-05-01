# Programma, kas veic masīva kārtošanu dilstoša secībā ar trīm metodēm
# Programmas autors Simona Bļinova
# Versija 1.0

import funkcijas
import random
import copy
import numpy

''' Funkciju bloks '''

def aizpildit_masivu(a, elementu_skaits):
    for i in range(elementu_skaits, 2, -1):
        b = random.randint(1, i-1)
        c = a[i]
        a[i] = a[b]
        a[b] = c

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

##### Ātrā jeb Hoara kārtošana #####

def hoara(a, sakuma_vertiba, beigu_vertiba):
    if sakuma_vertiba < beigu_vertiba:
        i = sakuma_vertiba
        j = beigu_vertiba
        solis = -1
        lv = True
        
        while i != j:
            a[0] += 1
            if lv == (a[i] < a[j]):
                x = a[i]
                a[i] = a[j]
                a[j] = x

                x = i
                i = j
                j = x

                lv = not lv
                solis = -solis

            j += solis

        hoara(a, sakuma_vertiba, i - 1)
        hoara(a, i + 1, beigu_vertiba)

    return a

##### Saliešanas metode #####

def saliesana(a, sakuma_vertiba, beigu_vertiba):
    garums = len(a)
    b = funkcijas.masiva_izveide(garums)
    if sakuma_vertiba < beigu_vertiba:
        vidus_vertiba = (sakuma_vertiba + beigu_vertiba) // 2
        saliesana(a, sakuma_vertiba, vidus_vertiba)
        saliesana(a, vidus_vertiba + 1, beigu_vertiba)

        for i in range(sakuma_vertiba, beigu_vertiba + 1):
            b[i] = a[i]

        i = sakuma_vertiba
        j = vidus_vertiba + 1
        k = sakuma_vertiba

        while i <= vidus_vertiba and j <= beigu_vertiba:
            a[0] += 1
            
            if b[i] > b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j += 1
            k += 1

        if j > beigu_vertiba:
            while i <= vidus_vertiba:
                a[k] = b[i]
                i += 1
                k += 1

    return a

##### Timsort #####

def iev_met(a, sakums, beigas):
    for i in range(sakums+1, beigas+1):
        elem = a[i]
        j = i-1
        while j >= sakums and a[j] < elem:
            a[0] += 1
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = elem


def apvienosana(a, sakums, vidus, beigas):
    g1 = vidus - sakums + 1
    g2 = beigas - vidus
    viens_a = numpy.copy(a[sakums:sakums+g1])
    otrs_a = numpy.copy(a[vidus+1:vidus+1+g2])
    i = 0
    j = 0
    k = sakums
    while i < g1 and j < g2:
        a[0] += 1
        if viens_a[i] >= otrs_a[j]:
            a[k] = viens_a[i]
            i += 1
        else:
            a[k] = otrs_a[j]
            j += 1
        k += 1
            
    while i < g1:
        a[k] = viens_a[i]
        i += 1
        k += 1
        
    while j < g2:
        a[k] = otrs_a[j]
        j += 1
        k += 1 


def tim_sort(a):
    INTERVALA_GARUMS = 2
    n = len(a)
    
    #Atsevišķu intervālu sakārtošana
    for i in range(1, n, INTERVALA_GARUMS):
        iev_met(a, i, min(i+INTERVALA_GARUMS - 1, n-1))
        
    izmers = INTERVALA_GARUMS
    while izmers < n:
        for sakums in range(1, n, 2*izmers):
            vidus = min(n-1, sakums+izmers-1)
            beigas = min(n-1, sakums + 2*izmers-1)
            if vidus < beigas:
                apvienosana(a, sakums, vidus, beigas)
        izmers = izmers * 2

    return a


''' Masīva izveides un aizpildes bloks '''

n = input('Ievadiet masīva izmēru --> ')
n = funkcijas.naturals_skaitlis(n)

masivs = funkcijas.masiva_izveide(n+1)

masivs = aizpildit_masivu(masivs, n)
print(masivs)

'''Masīva kopijas kārtošana trīs veidos'''

hoara_masivs = hoara(copy.deepcopy(masivs), 1, len(masivs)-1)

saliesanas_masivs = saliesana(copy.deepcopy(masivs), 1, len(masivs)-1)

timsort_masivs = tim_sort(copy.deepcopy(masivs))

''' Rezultātu izvade '''

print(f'Ātrā jeb Hoara kārtošanas metode: {izvade(hoara_masivs)}')
print(f'Saliešanas metode: {izvade(saliesanas_masivs)}')
print(f'Timsort metode: {izvade(timsort_masivs)}')