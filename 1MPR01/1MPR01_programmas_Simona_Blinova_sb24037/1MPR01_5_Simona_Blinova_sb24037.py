# Programma, kas atrod visus Mersena skaitus līdz 2*10^28.
# Programmas autors Simona Bļinova
# Versija 1.0

import funkcijas

'''Skaitļu aprēķina un pārbaudes bloks'''

mazakais_pirmskaitlis = 2

while mazakais_pirmskaitlis < 2*pow(10, 28):
    if funkcijas.vai_pirmskaitlis(mazakais_pirmskaitlis) == True:
        iespejamais_mersena_skaitlis = 2**mazakais_pirmskaitlis - 1
        if funkcijas.vai_pirmskaitlis(iespejamais_mersena_skaitlis) == True:
            print(iespejamais_mersena_skaitlis)
    
    mazakais_pirmskaitlis += 1
