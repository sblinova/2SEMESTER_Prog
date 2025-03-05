import funkcijas
import numpy
import math


def linearas_korelacijas_koeficients(a, b, n):
    x = funkcijas.videjais_aritmetiskais(a)
    y = funkcijas.videjais_aritmetiskais(b)

    summa1 = 0
    summa2 = 0
    summa3 = 0

    for i in range(n):
        summa1 += (a[i] - x) * (b[i] - y)
        summa2 += (a[i] - x) * (a[i] - x)
        summa3 += (b[i] - y) * (b[i] - y)
        
        if summa2 == 0 or summa3 == 0:
            return 'Kļūda, dalīšana ar nulli'

    return summa1 / math.sqrt(summa2 * summa3)


n = input('Ievadiet masīvu izmēru --> ')
n = funkcijas.naturals_skaitlis(n)

noverojumi1 = numpy.arange(n)
noverojumi2 = numpy.arange(n)

for i in range(n):
    skaitlis = input('Ievadiet skaitli 1. masīvā --> ')
    skaitlis = funkcijas.reals_skaitlis(skaitlis)
    noverojumi1[i] = skaitlis

    skaitlis = input('Ievadiet skaitli 2. masīvā --> ')
    skaitlis = funkcijas.reals_skaitlis(skaitlis)
    noverojumi2[i] = skaitlis

print(f'Lineāras korelācijas koeficients: {linearas_korelacijas_koeficients(noverojumi1, noverojumi2, n)}')