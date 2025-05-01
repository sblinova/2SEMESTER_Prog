# Programma, kas atrod masīva datu modu
# Programmas autors Simona Bļinova
# Versija 1.0

import funkcijas

def ievietosanas_metode(a):
    garums = len(a)

    for i in range(1, garums):
        if a[i-1] > a[i]:
            x = a[i]
            j = i

            while a[j-1] > x:
                a[j] = a[j-1]
                j -= 1
                if j == 0:
                    break
                
            a[j] = x

    return a

def moda(a):
    garums = len(a)

    saraksts = []
    i = 1
    skaits = 1
    moda = a[i-1]

    while i < garums:
        if moda != a[i]:
            saraksts.append((moda, skaits))
            moda = a[i]
            skaits = 1
        else:
            skaits += 1
        i += 1

    saraksts.append((moda, skaits))

    return saraksts

n = input('Ievadiet masīva garumu --> ')
n = funkcijas.naturals_skaitlis(n)

masivs = funkcijas.masiva_izveide(n)

masivs = funkcijas.datu_ievade_masiva(masivs)
# print(masivs)

sakartots_masivs = ievietosanas_metode(masivs)
print(sakartots_masivs)

modas = moda(sakartots_masivs)
# print(modas)

garums = len(modas)

if garums == n:
    print('Moda netika atrasta')
else:
    max_moda = modas[0][1]
    moda_indekss = 0 
    for i in range(1, garums):
        if max_moda < modas[i][1]:
            max_moda = modas[i][1]
            moda_indekss = i
    
    modu_saraksts = []
    modu_saraksts.append(modas[moda_indekss][0])
    for i in range(garums):
        if i != moda_indekss:
            if max_moda == modas[i][1]:
                modu_saraksts.append(modas[i][0])

# print(modu_saraksts)

    modu_virkne = ''

    for i in range(len(modu_saraksts)):
        modu_virkne += str(modu_saraksts[i]) + ' '

    print('Skaitļu kopas moda: ' + modu_virkne)