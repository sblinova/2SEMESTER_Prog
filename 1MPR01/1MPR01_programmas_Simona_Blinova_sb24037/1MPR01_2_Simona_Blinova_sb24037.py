# Programma, kas atrod vienādojuma ax^3+by^2+cz+d=0 visus atrisinājumus veselos skaitļos intervālā [-10, 10]
# Programmas autors Simona Bļinova
# Versija 1.0

import funkcijas

'''Koeficientu ievades un pārbaudes bloks'''

koeficients_a = input('Ievadiet veselo koeficientu a --> ')
koeficients_a = funkcijas.vesels_skaitlis(koeficients_a)

koeficients_b = input('Ievadiet veselo koeficientu b --> ')
koeficients_b = funkcijas.vesels_skaitlis(koeficients_b)

koeficients_c = input('Ievadiet veselo koeficientu c --> ')
koeficients_c = funkcijas.vesels_skaitlis(koeficients_c)

koeficients_d = input('Ievadiet veselo koeficientu d --> ')
koeficients_d = funkcijas.vesels_skaitlis(koeficients_d)


'''Cikls atrisinājumu mēklēšanai'''

for x in range(-10, 11):
    for y in range(11):
        cz = koeficients_a*x*x*x + koeficients_b*y*y + koeficients_d
        if koeficients_c != 0:
            z = int(round(cz/koeficients_c))
        else:
            z = 0
        if cz + z*koeficients_c == 0:
            print(f'({x}, {y}, {z})')
