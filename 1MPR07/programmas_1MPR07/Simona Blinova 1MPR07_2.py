# Programma, kas veic naturālo skaitļu saskaitīšanu
# Programmas autors Simona Bļinova
# Versija 1.0

import numpy

def parbaude(a):
    skaititajs = 1
    while skaititajs < 3:
        for i in range(len(a)):
            if ord(a[i]) < 48 or ord(a[i]) > 57:
                break
        else:
            return a
        skaititajs += 1
        a = input('Ievadiet skaitli vēlreiz --> ')
    else:
        print('Skaitlis netika ierakstīts, programma beidz darbību.')
        exit()
    
def masivs(a):
    g = len(a)
    b = numpy.arange(g)
    b = numpy.array(b, dtype='i')
    return b

def virkne_masivs(a, b):
    for i in range(len(b)):
        a[i] = b[len(b)-1-i]   
    return a
    
def masivs_virkne(a):
    c = ''
    for i in range(len(a)):
        c += str(a[len(a)-1-i]) 
    return c
        
# Pārbaude ka sakumā nav nulle
sk1 = input('Ievadiet pirmo skaitli --> ')
sk1 = parbaude(sk1)

sk2 = input('Ievadiet otro skaitli --> ')
sk2 = parbaude(sk2)

m1 = masivs(sk1)
m2 = masivs(sk2)

m1 = virkne_masivs(m1, sk1)
m2 = virkne_masivs(m2, sk2)

#print(m1)
#print(m2)

g1 = len(m1)
g2 = len(m2)

if g1 <= g2:
    maz_sk = m1
    liel_sk = m2
else:
    maz_sk = m2
    liel_sk = m1
    
m3 = masivs(liel_sk)

for i in range(len(maz_sk)):
    cip = maz_sk[i] + liel_sk[i]
    atl = cip // 10
    if atl != 0:
        cip -= atl*10
        if i+1 < len(liel_sk):
            liel_sk[i+1] += atl
        else:
            liel_sk = numpy.append(liel_sk, atl)
            m3 = numpy.append(m3, 0)
    m3[i] = cip
else:
    for i in range(len(maz_sk), len(liel_sk)):
        m3[i] = liel_sk[i]
    
sk3 = masivs_virkne(m3)

print(f'{sk1} + {sk2} = {sk3}')
    


    
    
        