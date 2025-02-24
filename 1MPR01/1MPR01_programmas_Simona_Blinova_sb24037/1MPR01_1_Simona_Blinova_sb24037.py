# Programma, kas nodrukā Paskāla trijstūri uz ekrāna. Rindu skaitu nosaka lietotājs.
# Programmas autors Simona Bļinova
# Versija 2.2

import funkcijas

'''Ievades un ievades pārbaudes bloks'''

rindu_skaits = input('Ievadiet Paskāla trijstūra rindu skaitu --> ')
rindu_skaits = funkcijas.naturals_skaitlis(rindu_skaits)


'''Bloks atstarpju skaita aprēķinam'''

# Atstarpes starp skaitliem
lielaka_skaitla_kartas_numurs = rindu_skaits // 2
lielakais_skaitlis = int(funkcijas.kombinacija(rindu_skaits, lielaka_skaitla_kartas_numurs))
lielaka_skaitla_garums = len(str(lielakais_skaitlis))

# Atstarpes pirms pirma rindas elementa
pedeja_rinda = ''
for kartas_numurs in range(rindu_skaits): # kartas numuru skaits ir vienāds ar rindas kārtas numuru
    kombinacijas_vertiba = int(funkcijas.kombinacija(rindu_skaits-1, kartas_numurs))
    pedeja_rinda = pedeja_rinda + str(kombinacijas_vertiba)
    if rindu_skaits-1 != kartas_numurs:
        pedeja_rinda = pedeja_rinda + ' ' * lielaka_skaitla_garums

pedejas_rindas_garums = len(pedeja_rinda)


'''Bloks Paskāla trijstūra izvadei'''

rinda = ''
for rindas_numurs in range(rindu_skaits-1):
    for kartas_numurs in range(rindas_numurs+1):
        kombinacijas_vertiba = int(funkcijas.kombinacija(rindas_numurs, kartas_numurs))
        rinda = rinda + str(kombinacijas_vertiba)
        if rindas_numurs != kartas_numurs:
            rinda = rinda + ' ' * lielaka_skaitla_garums
    rindas_garums = len(rinda)
    atstarpju_skaits = pedejas_rindas_garums - rindas_garums
    sakuma_atsarpju_skaits = atstarpju_skaits // 2
    rinda = ' ' * sakuma_atsarpju_skaits + rinda
    print(rinda)
    rinda = ''

print(pedeja_rinda)




