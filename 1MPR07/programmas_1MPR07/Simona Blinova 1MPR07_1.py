# Programma, kas veic lietotāja ievadīta vārda mēklēšanu vārda masīvā
# Programmas autors Simona Bļinova
# Versija 1.0

import numpy
import random

def kartosana(a, sv, bv):
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            g1 = len(a[i])
            g2 = len(a[j])
            
            if g1 < g2:
                mg = g1
            else:
                mg = g2
                
            b = 0
            for l in range(mg):
                if a[i][l] != a[j][l]:
                    b = l
                    break
            
            if lv == (ord(a[i][b]) > ord(a[j][b])):
                x = a[i]
                a[i] = a[j]
                a[j] = x
                x = i
                i = j
                j = x
                lv = not lv
                solis = -solis
            j = j + solis
        kartosana(a, sv, i-1)
        kartosana(a, i+1, bv)
        
def meklet(a, b):
    l = 0
    r = len(a) - 1
    while (l <= r):
        i = (l+r) // 2
        #print(l)
        #print(r)
        #print(a[i])
        #print(b)
        paz = burts_indeks(a[i], b)
        #print(paz)
        
        g1 = len(a)
        g2 = len(b)
        if g1 < g2:
            mg = g1
        else:
            mg = g2
    
        for n in range(mg):
            if a[i][n] != b[n]:
                paz = n
                break
        else:
            if len(a[i]) == mg:
                l = i + 1
            else:
                r = i - 1
        
        if a[i] == b:
            break
        elif ord(a[i][n]) < ord(b[n]):
            l = i + 1
        else:
            r = i - 1
    
    if a[i] == b:
        return i
    else:
        return -1
    
def burts_indeks(a, b):
    g1 = len(a)
    g2 = len(b)
    if g1 < g2:
        mg = g1
    else:
        mg = g2
        
    for i in range(mg):
        if a[i] != b[i]:
            paz = i
            break
    else:
        if mg == len(a):
            paz = True
        else:
            paz = False
            
    return paz
    
        
vardi = numpy.arange(10000)
vardi = numpy.array(vardi, dtype='U')
n = 0

while n < 10000:
    garums = random.randint(3, 8)
    vards = ''
    for i in range(garums):
        burts = random.randint(65, 90)
        vards += chr(burts)
    vardi[n] = vards
    n += 1
    
print(vardi)
        
kartosana(vardi, 0, len(vardi)-1)
print(vardi)

#print(vardi[2005])

v = input('Ievadiet burtu virkni (3-8 gara) --> ')
if v.isalpha() == True:
    v = v.upper()
#print(v)

if len(v) < 3 or len(v) > 8:
    print('Burtu virknē ir nepareizs burtu skaits!')
else:
    vieta = meklet(vardi, v)
    
    if vieta == -1:
        print(f'{v} netika atrasts masīvā.')
    else:
        print(f'{v} tika atrasts masīvā {vieta}.vietā.')
