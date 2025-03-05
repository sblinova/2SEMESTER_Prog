import numpy
import funkcijas


# Masīva izveides funkcija
def masiva_izveide(n):
    return numpy.arange(n)


# Datu ievades masīvā funkcija
def datu_ievade_masiva(a):
    garums = len(a)
    for i in range(garums):
        vertiba = input('Ievadiet vērtību --> ')
        # pārbaude lai reāls, lai varētu atrast min un max
        vertiba = funkcijas.reals_skaitlis(vertiba)
        a[i] = vertiba
    return a


# Datu izvades funkcija
def datu_izvade(a):
    print(a)


# Masīva mazākas vērtības atrašanas funkcija
def mazaka_vertiba(a):
    garums = len(a)
    for i in range(garums):
        if i == 0:
            mazakais = a[i]
        else:
            if mazakais > a[i]:
                mazakais = a[i]
    return mazakais


# Masīva lielākas vērtības atrašanas funkcija
def lielaka_vertiba(a):
    garums = len(a)
    for i in range(garums):
        if i == 0:
            lielakais = a[i]
        else:
            if lielakais < a[i]:
                lielakais = a[i]
    return lielakais


n = input('Ievadiet elementu skaitu masīvā --> ')
n = funkcijas.reals_skaitlis(n)

masivs = masiva_izveide(n)
masivs = datu_ievade_masiva(masivs)
datu_izvade(masivs)
print(f'Mazāka vērtība masīva: {mazaka_vertiba(masivs)}')
print(f'Lielāka vērtība masīva: {lielaka_vertiba(masivs)}')