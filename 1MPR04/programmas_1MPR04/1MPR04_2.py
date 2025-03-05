import funkcijas
import numpy
import math


def videjais_aritmetiskais(a):
    garums = len(a)
    summa = 0

    for i in range(garums):
        summa += a[i]
    
    return summa / garums


def videja_kvadratiska_vertiba(a):
    garums = len(a)
    summa = 0

    for i in range(garums):
        summa += a[i]*a[i]

    return math.sqrt(summa / garums)


def videja_harmoniska_vertiba(a):
    garums = len(a)
    summa = 0

    for i in range(garums):
        if a[i] != 0:
            summa += 1 / a[i]
        else:
            garums -= 1
    
    return garums / summa


def videja_geometriska_vertiba(a):
    garums = len(a)
    reizinajums = 1

    for i in range(garums):
        reizinajums *= a[i]

    return reizinajums ** (1/garums)


def videjas_lineara_novirze(a):
    garums = len(a)
    summa = 0

    x = videjais_aritmetiskais(a)

    for i in range(garums):
        summa += abs(a[i] - x)

    return summa / garums


def standartnovirze(a):
    garums = len(a)
    summa = 0

    x = videjais_aritmetiskais(a)

    for i in range(garums):
        summa += (a[i] - x) * (a[i] - x)

    return math.sqrt(summa / garums)


n = input('Ievadiet skaitļu skaitu --> ')
n = funkcijas.naturals_skaitlis(n)

saraksts = numpy.arange(n)

for i in range(n):
    skaitlis = input('Ievadiet skaitli --> ')
    skaitlis = funkcijas.naturals_skaitlis(skaitlis)
    saraksts[i] = skaitlis

# print(saraksts)
print(f'Vidējais aritmētiskais: {videjais_aritmetiskais(saraksts)}')
print(f'Vidējais kvadrātiskais: {videja_kvadratiska_vertiba(saraksts)}')
print(f'Vidējais harmoniskais: {videja_harmoniska_vertiba(saraksts)}')
print(f'Vidējais ģeometriskais: {videja_geometriska_vertiba(saraksts)}')
print(f'Vidējā lineāra novirze: {videjas_lineara_novirze(saraksts)}')
print(f'Standartnovirze: {standartnovirze(saraksts)}')