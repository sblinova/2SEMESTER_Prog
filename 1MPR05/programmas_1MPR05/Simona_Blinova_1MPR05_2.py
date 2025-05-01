# Programma, kas atrod masīva datu mediānu
# Programmas autors Simona Bļinova
# Versija 1.2

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

n = input('Ievadiet masīva garumu --> ')
n = funkcijas.naturals_skaitlis(n)

masivs = funkcijas.masiva_izveide(n)

masivs = funkcijas.datu_ievade_masiva(masivs)
#print(masivs)

masivs = ievietosanas_metode(masivs)
print(masivs)

videjais_indekss = n // 2

if n % 2 == 0:
    vertibu_summa = masivs[videjais_indekss] + masivs[videjais_indekss-1]
    mediana = vertibu_summa / 2
else:
    mediana = masivs[videjais_indekss]

print(f'Kopas mediāna: {mediana}')
    
