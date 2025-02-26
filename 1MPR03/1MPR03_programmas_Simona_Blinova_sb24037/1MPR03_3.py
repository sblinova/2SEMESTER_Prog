def perlisu_daudzums(rindas, zilas, sarkanas, oranzas):
    if rindas == 0:
        return zilas, sarkanas, oranzas
    
    zilas_rinda = zilas + 2 * sarkanas + 3 * oranzas
    sarkanas_rinda = 2 * zilas + 3 * sarkanas + oranzas
    oranzas_rinda = 3 * zilas + 2 * sarkanas + oranzas

    return perlisu_daudzums(rindas-1, zilas_rinda, sarkanas_rinda, oranzas_rinda)

rindas = int(input('Ievadiet rindu skaitu --> '))
krasa = input('Ievadiet sākuma krāsu (z, s, o) --> ')

zilas = 0
sarkanas = 0
oranzas = 0

match krasa:
    case 'z':
        zilas, sarkanas, oranzas = perlisu_daudzums(rindas, 1, sarkanas, oranzas)
    case 's':
        zilas, sarkanas, oranzas = perlisu_daudzums(rindas, zilas, 1, oranzas)
    case 'o':
        zilas, sarkanas, oranzas = perlisu_daudzums(rindas, zilas, sarkanas, 1)
    case _:
        print('Tādas krāsas nav!')

print(f'{rindas}. rindā zilo pērlīšu skaits ir {zilas}, sarkano - {sarkanas}, oranžo - {oranzas}.')
