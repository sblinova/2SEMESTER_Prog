# Programma, kas aprēķina arcsin(x) vērtību ar precizitāti 10^-6 
# Programmas autors Simona Bļinova
# Versija 2.1

'''Funkciju bloks'''

# Funkcija, lai pārbaudītu ievades korektību
def vertibas_intervals(a):
    # meģinājumu skaita skaitītājs (3 meģinājumi ierakstam)
    meginajumi = 1
    while meginajumi <= 3:
        try:
            a = float(a)
            if a < 1 and a > -1:
                return float(a)
            else:
                raise Exception
        except:
            if meginajumi < 3:
                meginajumi += 1
                a = input('Ievadiet x vērtību (|x| < 1) vēlreiz --> ')
            else:
                print('Programma beidz darbību!')
                exit()


'''Lietotāja ievades un datu pārabaudes bloks'''
x = input('Ievadiet x vērtību (|x| < 1) --> ')
x = vertibas_intervals(x)


'''Izteiksmes aprēķina un precizitātes pārbaudes bloks'''  
precizitate = 1e-6  
saskaitamais = x  
summa = saskaitamais 

# Katra sskaitama sākuma sastāvdaļas
x_dala_saucejs = 1
x_dala_skaititajs = x
koeficientu_dala_saucejs = 1
koeficientu_dala_skaititajs = 1
pakape = 3
    
while abs(saskaitamais) >= precizitate:
    # Cikls, kas noskaidro un piereizina skaitļus skaititājam vai saucējam, pirms daļas ar x vērtību kādā pakāpē
    for skaitlis in range(1, pakape):
        if skaitlis % 2 == 0:
            koeficientu_dala_saucejs *= skaitlis
        else:
            koeficientu_dala_skaititajs *= skaitlis

        x_dala_saucejs = pakape
        x_dala_skaititajs = x_dala_skaititajs * x * x
        saskaitamais = (koeficientu_dala_skaititajs/koeficientu_dala_saucejs) * (x_dala_skaititajs/x_dala_saucejs)
        summa += saskaitamais
        pakape += 2

print(f'arcsin({x})={summa}')


        