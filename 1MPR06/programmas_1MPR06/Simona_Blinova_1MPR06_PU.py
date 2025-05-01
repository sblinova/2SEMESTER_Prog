# Programma, kas veic trīs dažāda izmēra masīvu apvienošanu
# Programmas autors Simona Bļinova
# Versija 1.0

import funkcijas
import math
import random

def izveidot_masivu():
    n = input('Ievadiet masīva izmēru --> ')
    n = funkcijas.naturals_skaitlis(n)

    a = funkcijas.masiva_izveide(n)

    for i in range(n):
        skaitlis = input('Ievadiet skaitli masīvā --> ')
        skaitlis = funkcijas.reals_skaitlis(skaitlis)
        a[i] = skaitlis

    return a


def shell_metode_augosa(a):
    garums = len(a)

    solis = (3**math.floor(math.log(2*garums+1, 3))-1)//2

    while solis >= 1:
        for i in range(0, solis):
            for j in range(solis+i, garums, solis):
                
                if a[j-solis] > a[j]:
                    b = a[j]
                    k = j

                    while a[k-solis] > b:
                        a[k] = a[k-solis]
                        k -= solis
                        if k == i:
                            break
                    
                    a[k] = b
                  
        solis = (solis - 1) // 3

    return a


def shell_metode_dilstosa(a):
    garums = len(a)

    solis = (3**math.floor(math.log(2*garums+1, 3))-1)//2

    while solis >= 1:
        for i in range(0, solis):
            for j in range(solis+i, garums, solis):
                
                if a[j-solis] < a[j]:
                    b = a[j]
                    k = j

                    while a[k-solis] < b:
                        a[k] = a[k-solis]
                        k -= solis
                        if k == i:
                            break
                    
                    a[k] = b
                  
        solis = (solis - 1) // 3

    return a


def apvienosana(a, b):
    garums_a = len(a)
    garums_b = len(b)
    garums_c = garums_a + garums_b

    c = funkcijas.masiva_izveide(garums_c)

    # Nosaka indeksu (vai ir augoša vai dilstoša)
    ia = indeksa_noteiksana(a)
    ib = indeksa_noteiksana(b)
    ic = 0

    # pārveido masīvus par augošu, ja noteikts, ka ir dilstoša
    if ia != 0:
        a = shell_metode_augosa(a)
        ia = 0
    
    if ib != 0:
        b = shell_metode_augosa(b)
        ib = 0

    while ia < garums_a and ib < garums_b:
        if a[ia] < b[ib]:
            c[ic] = a[ia]
            ia += 1
        else:
            c[ic] = b[ib]
            ib += 1
        ic += 1

    if ia < garums_a:
        for i in range(ia, garums_a):
            c[ic] = a[i]
            ic += 1
    else:
        for i in range(ib, garums_b):
            c[ic] = b[i]
            ic += 1

    return c


def indeksa_noteiksana(a):
    garums = len(a)

    if a[0] < a[garums-1]:
        i = 0
    else:
        i = garums-1
    
    return i


def random_sort(a):
    # Ja 0, tad dilstoša
    # Ja 1, tad augoša
    pazime = random.randint(0, 1)

    if pazime == 0:
        return shell_metode_dilstosa(a)
    else:
        return shell_metode_augosa(a)


masivs1 = izveidot_masivu()
print(masivs1)

masivs2 = izveidot_masivu()
print(masivs2)

masivs3 = izveidot_masivu()
print(masivs3)

masivs1 = random_sort(masivs1)
masivs2 = random_sort(masivs2)
masivs3 = random_sort(masivs3)

print(masivs1, masivs2, masivs3)

masivs12 = apvienosana(masivs1, masivs2)
masivs = apvienosana(masivs12, masivs3)
print(masivs)