# Programma, kas veic naturālo skaitļu atņemšānu
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

if g1 == g2:
    for i in range(g1):
        if m1[g1-1-i] == m2[g2-1-i]:
            maz_sk = m2
            liel_sk = m1            
            continue
        elif m1[g1-1-i] < m2[g2-1-i]:
            maz_sk = m1
            liel_sk = m2
        else:
            maz_sk = m2
            liel_sk = m1        
elif g1 < g2:
    maz_sk = m1
    liel_sk = m2
else:
    maz_sk = m2
    liel_sk = m1
    
m3 = masivs(liel_sk)

for i in range(len(maz_sk)):
    if liel_sk[i] < maz_sk[i]:
        for j in range(i+1, len(liel_sk)):
            if liel_sk[j] != 0:
                n = j
                break
        for k in range(n, i, -1):
            liel_sk[k] -= 1
            liel_sk[k-1] += 10
    #print(liel_sk)
    cip = liel_sk[i] - maz_sk[i]
    m3[i] = cip
    #print(cip)
else:
    for i in range(len(maz_sk), len(liel_sk)):
        m3[i] = liel_sk[i]
        
indeksi = []
for i in range(len(m3)-1, 0, -1):
    if m3[i] != 0:
        bv = i
        break
    else:
        indeksi.append(i)
        
#print(m3)
m3 = numpy.delete(m3, indeksi)
#print(m3)
    
sk3 = masivs_virkne(m3)

if int(sk1) < int(sk2):
    a = sk1
    b = sk2
else:
    a = sk2
    b = sk1

print(f'{b} - {a} = {sk3}')
