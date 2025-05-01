# Programma, kas veic determinanta apreķinu
# Programmas autors Simona Bļinova
# Versija 1.0

import numpy

def izveidot_matricu(a, b):
    c = numpy.empty((a, b))
    for i in range(a):
        for j in range(b):
            c[i, j] = int(input('Ievadiet matricas '+str(i+1)+'.rindas '+str(j+1)+'.kolonnas skaitli --> '))
    return c    


def determinants(a):
    n = a.shape[0]
    n1 = a.shape[1]
    if n != n1:
        return 'šī nav kvadrātiskā matrica, nevar aprēķināt determinantu.'
    det = 1
    for u in range(n):
        if a[u, u] == 0:
            k = u
            while a[k, u] == 0:
                k += 1
                if k >= n:
                    return 0
            det = -det
            for i in range(n):
                x = a[u, i]
                a[u, i] = a[k, i]
                a[k, i] = x
        det = det * a[u, u]
        for j in range(n-1, u-1, -1):
            a[u, j] = a[u, j] / a[u, u]
        for i in range(u+1, n):
            for j in range(n-1, u-1, -1):
                a[i, j] = a[i, j] - a[i, u] * a[u, j]
    return f'det = {det}'

n = int(input('Ievadiet matricas rindu skaitu --> '))
m = int(input('Ievadiet matricas kolonnu skaitu --> '))

matrica = izveidot_matricu(n, m)

print(determinants(matrica))
