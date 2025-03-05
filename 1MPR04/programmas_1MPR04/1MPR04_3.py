import numpy
import funkcijas

def videja_sverta(x, y):
    summa1 = 0
    summa2 = 0

    for i in range(len(x)):
        summa1 += x[i]*y[i]
        summa2 += x[i]

    return summa1 / summa2

n = input('Ievadiet masīvu izmēru --> ')
n = funkcijas.naturals_skaitlis(n)

vertibas = numpy.arange(n)
skaits = numpy.arange(n)

for i in range(n):
    vertiba = input('Ieadiet vērtību --> ')
    vertiba = funkcijas.reals_skaitlis(vertiba)
    vertibas[i] = vertiba

    vertibas_skaits = input('Ieadiet vērtības skaitu --> ')
    vertibas_skaits = funkcijas.naturals_skaitlis(vertibas_skaits)
    skaits[i] = vertibas_skaits

print(f'Vidēja svērta vērtība: {videja_sverta(vertibas, skaits)}')

