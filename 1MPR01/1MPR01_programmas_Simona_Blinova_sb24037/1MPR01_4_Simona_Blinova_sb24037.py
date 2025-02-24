# Programma, kas nodrukā visus laimīgos pasta zīmogus kopš Kristus dzimšanas.
# Programmas autors Simona Bļinova
# Versija 1.0

import funkcijas

'''Cikls datumu pārbaudei un izvadei'''

for gads in range(1, 10000):
    datums_gads = funkcijas.nulles(gads, 'g')
    # print(datums_gads)
    for menesis in range(1, 13):
        datums_menesis = funkcijas.nulles(menesis, 'm')
        # print(datums_menesis)

        # match case, kas nosaka dienu skaitu menesī
        match menesis:
            case 1 | 3 | 5 | 7 | 8 | 10| 12:
                dienas = 31
            case 4 | 6 | 9 | 11:
                dienas = 30
            case 2:
                if gads % 4000:
                    dienas = 28
                elif gads % 400:
                    dienas = 29
                elif gads % 100:
                    dienas = 28
                elif gads % 4:
                    dienas = 29
                else:
                    dienas = 28

        for diena in range(1, dienas+1):
            datums_diena = funkcijas.nulles(diena, 'd')

            # Tiek ierakstīta simbolu virkne ar apgrieztu meneša un dienas vērtību
            parbaudes_dala = datums_menesis[::-1] + datums_diena[::-1]
            # print(parbaudes_dala)

            if parbaudes_dala == datums_gads:
                print(f'{datums_diena}.{datums_menesis}.{datums_gads}')